#!/usr/bin/env python


import ringdown
import pycbc.filter
import numpy as np
from gwpy.timeseries import TimeSeries
from pycbc.types.timeseries import TimeSeries as PyCBCTimeSeries
from pycbc.psd import interpolate
from matplotlib import pyplot as plt
import sys

#ligo-proxy-init georgia.stevens


inputarg = 'run2'

# Defining the Exepected Glitch Signal Time and Times surrounding it
glitchtime = 1165577780
addedtime = 128
gpsstart = glitchtime - addedtime
gpsend = glitchtime + addedtime
duration = (addedtime*2)
samplerate = 16384


# fetch the open data from GWOSC
data = TimeSeries.find(
    "H1:DCS-CALIB_STRAIN_C02", # the channel name
    gpsstart,  # the GPS start time
    gpsend,  # the GPS end time
)


#alternatively
'''
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
'''

# convert the data to a PyCBC time series
pycbcdata = PyCBCTimeSeries(data.data, delta_t=(1 / data.sample_rate.value))

# high-pass filter the data to only include the frequencies we're interested in
lowcutoff = 1000
buffer = 50  # just allow a bit of a buffer at the edges
pycbcdata = pycbcdata.highpass_fir(lowcutoff - buffer, 8)  # 8 is the "order" of the filter



#split them because otherwise it's too big?
ranges = [[1300,1800],[1800,2400]]

for a in ranges:
    frange = a
    taurange = [0.05, 0.5]  
    mm = 0.03  
    tb = ringdown.RingdownTemplateBank(frange, taurange=taurange, mm=mm)
    flow = lowcutoff
    
    minf = str(int(np.amin(frange)))
    maxf = str(int(np.amax(frange)))    
    
    
    maximum_snr_of_template = []
    template_tau = []
    template_qs = []
    maximum_snr_of_chunk = []
    

    template_freq = np.array(tb.bank_freqs)
    template_tau.append(tb.bank_taus)
    template_qs.append(tb.bank_qs)
    
    
    respbuffer = 2
    chunkdur = 4
    
    runs = int(((duration - (respbuffer+chunkdur)) / respbuffer ))   
  
    for i in range(runs):


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
  
    
            hp, hc = waveform
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
        
        #np.concatenate((maximum_snr_of_chunk,maxvalue),axis=0)
        #np.concatenate((maximum_snr_of_template,maximum_snr_data),axis=0)
    
    
    
        respbuffer += 2
        chunkdur = 4

    


    
    maximumsnroverall = []
    ydata = maximum_snr_of_template

    for x in range(len(template_freq)):
        totaly = []
        for i in range(len(ydata)):
            totaly.append(ydata[i][x])
        maximumsnroverall.append(np.amax(totaly))
    
    

    
    
    
    name1 = "actualglitchtest_maximum_snr_of_template" + minf +"to"+ maxf + inputarg +".pkl"
    np.save(name1,maximumsnroverall,allow_pickle=True)
#    name2 = "glitchtest_maximum_snr_of_chunk" + minf +"to"+ maxf + inputarg +".pkl"
#    np.save(name2,maximum_snr_of_chunk,allow_pickle=True)
    name3 = "actualglitchtest_template_freq" + minf +"to"+ maxf + inputarg +".pkl"
    np.save(name3,template_freq,allow_pickle=True)
#    name4 = "glitchtest_template_tau" + minf +"to"+ maxf + ".pkl"
#    np.save(name4,template_tau,allow_pickle=True)
#    name5 = "glitchtest_template_qs" + minf +"to"+ maxf + ".pkl"
#    np.save(name5,template_qs,allow_pickle=True)
    
    
    
#adding the two freq sets of data together

total_frequencies = []
total_snrs = []


for a in ranges:
    minf = a[0]
    maxf = a[1]
    freqs = np.load('actualglitchtest_template_freq{a}to{b}{c}.pkl.npy'.format(a=minf,b=maxf,c=inputarg))
    snrs = np.load('actualglitchtest_maximum_snr_of_template{a}to{b}{c}.pkl.npy'.format(a=minf,b=maxf,c=inputarg))

    total_frequencies = np.concatenate((total_frequencies, freqs),axis=0)
    total_snrs = np.concatenate((total_snrs, snrs),axis=0)

name3 = "signaltotalfreqsuncut" + inputarg + ".pkl"
np.save(name3,total_frequencies,allow_pickle=True)
name4 = 'signaltotalsnrsuncut' + inputarg + ".pkl"
np.save(name4,total_snrs,allow_pickle=True)


#cutting the data in unreliable frequencies

cut_total_frequencies = []
cut_total_snrs = []

cutrange1 = [1452,1488]
cutrange2 = [2010,2020]
cutrange3 = [0,0]

for i in range(len(total_frequencies)):
    if (cutrange1[0] <= total_frequencies[i] <= cutrange1[1]) or (cutrange2[0] <= total_frequencies[i] <= cutrange2[1]) or (cutrange3[0] <= total_frequencies[i] <= cutrange3[1]) :
        continue
    else:
        cut_total_snrs.append(total_snrs[i])
        cut_total_frequencies.append(total_frequencies[i])
        
name5 = 'signaltotalfreqscut' + inputarg + ".pkl"
np.save(name5,cut_total_frequencies,allow_pickle=True)
name6 = 'signaltotalsnrscut' + inputarg + ".pkl"
np.save(name6,cut_total_snrs,allow_pickle=True)





