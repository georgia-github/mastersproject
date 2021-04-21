"""
Show creation of an injection and analysis of a matched-filter SNR for a
single template.
"""

import ringdown
import pycbc.filter
import numpy as np
from matplotlib import pyplot as plt


starttime = 1000000000.0  # start time of data
duration = 2.0  # duration of data
dt = 1.0 / 8192.0  # time step

tc = starttime + 0.5  # start time of the ring-down signal (GPS second)
freq = 1234.5  # frequency of signal (Hz)
amp = 5e-21  # amplitude of signal
tau = 0.07  # decay time (seconds)
ra = 0.3  # source right ascension (rads)
dec = -0.3  # source declination (rads)
psi = 1.1  # source polarisation angle (rads)
phi = 0.2  # initial phase (rads)
inclination = 0.9  # source inclination angle (rads)

detector = "H1"

# default PSD will be aLIGO design curve
injH1 = ringdown.RingdownInjections(
    tc,
    freq,
    amp,
    tau,
    ra,
    dec,
    psis=psi,
    phis=phi,
    inclinations=inclination,
    detector=detector,
    starttime=starttime,
    duration=duration,
    deltat=dt,
)

# get signal SNR
stilde_signal = injH1.injection_data.to_frequencyseries()  # pure signal in frequency domain
psdnonzero = np.where(injH1.psd.data[:len(stilde_signal)] != 0)  # indices for non-zero PSD
snr = np.sqrt((4 / duration) * np.sum(np.conj(stilde_signal.data[psdnonzero]) * stilde_signal.data[psdnonzero] / injH1.psd.data[psdnonzero])).real
#print("Signal optimal SNR is {0:.1f}".format(snr))

stilde = injH1.data.to_frequencyseries()

frange = [1200, 1250]  # frequency range (Hz)
taurange = [0.05, 0.07]  # Quality factor ranges
mm = 0.03  # maximum mismatch

tb = ringdown.RingdownTemplateBank(frange, taurange=taurange, mm=mm)
flow = 20.0


maximum_snr_data = []




for i, waveform in enumerate(tb.generate_waveforms(domain="frequency", deltaf=stilde.delta_f)):
    hp, hc = waveform

    hp.resize(len(stilde))
    snr2 = pycbc.filter.matched_filter(hp, stilde, psd=injH1.psd, low_frequency_cutoff=flow)

    
    
    snr_value_list = np.array(abs(snr2))
    maximum_snr_value = np.amax(snr_value_list, axis=0)
    maximum_snr_data.append(maximum_snr_value)
    index_of_maximum_snr_value = np.argmax(snr_value_list, axis=0)
    

    
    i+=1
        
frequencybank = np.array(tb.bank_freqs)
qbank = np.array(tb.bank_qs)
taubank = np.array(tb.bank_taus)
#print("Frequencys:",frequencybank)
#print("Q's:",qbank)
#print("Taus:",taubank)
#print(snr)        
#print(maximum_snr_data)        
fmin = frequencybank[0]
fmax = frequencybank[-1]   
taumin = taubank[0]
taumax = taubank[-1]

print('This data was made from, a frequency range:',fmin,'to',fmax,'with tau range',taumin,'to',taumax,'. It had a maximum optimal SNR value',maximum_snr_value,'.')        
        

        

xplot = frequencybank
area = np.divide(maximum_snr_data,snr/100) 

####################TAU-FREQ-GRAPH#################################################
'''
yplot = taubank
plt.scatter(xplot, yplot,s=area,c=area,marker='o',cmap="Blues",edgecolor="black")
plt.ylabel('Tau Value (s)')
plt.xlabel('Frequency (Hz)')
cbar = plt.colorbar()
cbar.set_label('Relative Strength of SNR')
plt.legend(['Maximum SNR Value from a given template'],loc="upper center")
plt.show()
plt.savefig('taufrequencygraph.png')
'''
#################################################################################


#####################SNR-FREQ-GRAPH##############################################
'''
y2plot = maximum_snr_data
plt.hlines(snr,fmin, fmax)
plt.scatter(xplot, y2plot,s=area,c=area,marker='o',cmap="Blues",edgecolor="black")
plt.ylabel('SNR')
plt.xlabel('Frequency (Hz)')
cbar = plt.colorbar()
cbar.set_label('Relative Strength of SNR')
plt.legend(['The optimal SNR value for a detection','Maximum SNR Value from a given template'],loc="center")
plt.show()
plt.savefig('snrfrequencygraph.png')
'''
##################################################################################


####################ORIGINAL-GRAPH################################################
'''
plt.plot(snr2.sample_times, abs(snr2))
plt.ylabel('signal-to-noise ratio')
plt.xlabel('time (s)')
plt.show()
plt.savefig('originalmatchedfilter.png')
'''
##################################################################################