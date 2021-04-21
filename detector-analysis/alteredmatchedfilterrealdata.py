"""
Show matched filter analysis on a portion of real detector data.
"""

import ringdown
import pycbc.filter
import numpy as np
from gwpy.timeseries import TimeSeries
from pycbc.types.timeseries import TimeSeries as PyCBCTimeSeries
from pycbc.psd import interpolate
from matplotlib import pyplot as plt


# download a 128 second chunk of data (the whole data length will be used to generate the
# power spectral density to get a good average)
duration = 128  # number of seconds of data to download
gpsstart = 1187008884  # end of GW170817, start time is 1187008880
gpsend = gpsstart + duration
samplerate = 16384

detector = "L1"

# fetch the open data from GWOSC
data = TimeSeries.fetch_open_data(
    detector,
    gpsstart,
    gpsend,
    sample_rate=samplerate,
    format='hdf5',
    host='https://www.gw-openscience.org',
    verbose=False,
    cache=True,
)



# convert the data to a PyCBC time series
pycbcdata = PyCBCTimeSeries(data.data, delta_t=(1 / data.sample_rate.value))

# high-pass filter the data to only include the frequencies we're interested in
lowcutoff = 1000
buffer = 50  # just allow a bit of a buffer at the edges
pycbcdata = pycbcdata.highpass_fir(lowcutoff - buffer, 8)  # 8 is the "order" of the filter



maximum_snr_of_template = []
template_freq = []
template_tau = []
template_qs = []


cutrange1 = [1210,1220]
cutrange2 = [1280,1290]






# create the template bank
frange = [1200, 1300]  # frequency range (Hz) 1230-1240 and 0.06-0.07 gives us like 7 templates
taurange = [0.05, 0.2]  # Quality factor ranges
mm = 0.03  # maximum mismatch
tb = ringdown.RingdownTemplateBank(frange, taurange=taurange, mm=mm)
flow = lowcutoff

maximum_snr_of_chunk = []

respbuffer = 2
chunkdur = 4
    
runs = int(((duration - (respbuffer+chunkdur)) / respbuffer ))   
  
for x in range(1):


    # get the initial chunk of data to matched filter - let's get four seconds
    # after ignoring the first two seconds due to the filter response

    inidata = pycbcdata.crop(respbuffer, duration - (respbuffer + chunkdur)) #amount to cut from left and amount to cut from right
    initilde = inidata.to_frequencyseries()

    # get the psd using the whole data segment (using 128 / 16 length segments)
    psd = pycbcdata.filter_psd(128 / 16, (8 / samplerate), flow)
    psd = interpolate(psd, initilde.delta_f)




    maximum_snr_data = []
    # perform matched filtering
    for i, waveform in enumerate(tb.generate_waveforms(domain="frequency", deltaf=initilde.delta_f)):
        if (cutrange1[0] <= tb.bank_freqs[i] <= cutrange1[1]) or (cutrange2[0] <= tb.bank_freqs[i] <= cutrange2[1]) : 
            continue
        else:
            template_freq.append(tb.bank_freqs)
            template_tau.append(tb.bank_taus)
            template_qs.append(tb.bank_qs)    
    
            hp, hc = waveform
            #print(waveform)
            hp.resize(len(initilde))
            snr = pycbc.filter.matched_filter(hp, initilde, psd=psd,
                                      low_frequency_cutoff=flow)

            # remove regions corrupted by filter wraparound (see https://pycbc.org/pycbc/latest/html/gw150914.html#calculate-the-signal-to-noise)
            snr = snr[len(snr) // 4: len(snr) * 3 // 4]

    
            snr_value_list_forthistemplate = np.array(abs(snr))
            maximum_snr_value_of_template = np.amax(snr_value_list_forthistemplate, axis=0)
            maximum_snr_data.append(maximum_snr_value_of_template)
    
    maxvalue = np.amax(maximum_snr_data, axis=0)
    maximum_snr_of_chunk.append(maxvalue)
    maximum_snr_of_template.append(maximum_snr_data)
    
    
    
    respbuffer += 2
    chunkdur = 4

    

minf = str(int(np.amin(frange)))
maxf = str(int(np.amax(frange)))    
    

name1 = "maximum_snr_of_template" + minf +"to"+ maxf + ".pkl"
np.save(name1,maximum_snr_of_template,allow_pickle=True)
name2 = "maximum_snr_of_chunk" + minf +"to"+ maxf + ".pkl"
np.save(name2,maximum_snr_of_chunk,allow_pickle=True)
name3 = "template_freq" + minf +"to"+ maxf + ".pkl"
np.save(name3,template_freq,allow_pickle=True)
name4 = "template_tau" + minf +"to"+ maxf + ".pkl"
np.save(name4,template_tau,allow_pickle=True)
name5 = "template_qs" + minf +"to"+ maxf + ".pkl"
np.save(name5,template_qs,allow_pickle=True)
name7 = "frange" + minf + maxf + ".pkl"
np.save(name7,frange,allow_pickle=True)
