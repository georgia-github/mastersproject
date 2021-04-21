#!/usr/bin/env python

import ringdown
import pycbc.filter
import numpy as np
from matplotlib import pyplot as plt
import sys

inputarg = sys.argv[1]

starttime = 1000000000.0  # start time of data
duration = 2.0  # duration of data
dt = 1.0 / 8192.0  # time step



detector = "H1"



frange = [1500, 3000]  # frequency range (Hz)
taurange = [0.05, 0.5]  # Quality factor ranges
mm = 0.03  # maximum mismatch

tb = ringdown.RingdownTemplateBank(frange, taurange=taurange, mm=mm)
flow = 20.0




maximum_noise_snrsignals = []
injected_signal_freq = []
injected_signal_tau = []
injected_signal_amp = []
injected_signal_optimal_snr = []
injected_signal_RA = []
injected_signal_DEC = []
injected_signal_inclination = []

for x in range(10):
    maximum_snr_data = []
    
    
    
    tc = starttime + 0.5  # start time of the ring-down signal (GPS second)
    freq = np.random.uniform(1500,3000)  # frequency of signal (Hz)
    injected_signal_freq.append(freq)
    amp = np.random.uniform(1e-23,5e-22)  # amplitude of signal
    injected_signal_amp.append(amp)
    tau = np.random.uniform(0.05,0.5)  # decay time (seconds)
    injected_signal_tau.append(tau)
    ra = np.random.uniform(0, 2 * np.pi)  # source right ascension (rads)
    injected_signal_RA.append(ra)
    dec = -(np.pi/2.) + np.arccos(np.random.uniform(-1, 1))     # source declination (rads)
    injected_signal_DEC.append(dec)
    psi = 1.1  # source polarisation angle (rads)
    phi = 0.2  # initial phase (rads)
    inclination = np.arccos(np.random.uniform(-1, 1))   # source inclination angle (rads)
    injected_signal_inclination.append(inclination)
    
    
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
    deltat=dt,)

    # get signal SNR
    stilde_signal = injH1.injection_data.to_frequencyseries()  # pure signal in frequency domain
    psdnonzero = np.where(injH1.psd.data[:len(stilde_signal)] != 0)  # indices for non-zero PSD
    snr = np.sqrt((4 / duration) * np.sum(np.conj(stilde_signal.data[psdnonzero]) * stilde_signal.data[psdnonzero] / injH1.psd.data[psdnonzero])).real
    injected_signal_optimal_snr.append(snr)
    #print("Signal optimal SNR is {0:.1f}".format(snr))

    stilde = injH1.data.to_frequencyseries()
    
    
    
    for i, waveform in enumerate(tb.generate_waveforms(domain="frequency", deltaf=stilde.delta_f)):
       
        hp, hc = waveform
        hp.resize(len(stilde))
        snr2 = pycbc.filter.matched_filter(hp, stilde, psd=injH1.psd, low_frequency_cutoff=flow)

    
        
        snr_value_list_forthistemplate = np.array(abs(snr2))
        maximum_snr_value_of_template = np.amax(snr_value_list_forthistemplate, axis=0)
        maximum_snr_data.append(maximum_snr_value_of_template)
        #index_of_maximum_snr_value = np.argmax(snr_value_list, axis=0)
    

    
        i+=1
        
    maxvalue = np.amax(maximum_snr_data, axis=0)
    maximum_noise_snrsignals.append(maxvalue)

    
    


compliedmaximum_noise_snrsignals = "maximumsnrsignal" + inputarg + ".pkl"  
np.save(compliedmaximum_noise_snrsignals, maximum_noise_snrsignals, allow_pickle=True)

compliedinjected_signal_freq = "injectedsignalfreq" + inputarg + ".pkl"  
np.save(compliedinjected_signal_freq, injected_signal_freq, allow_pickle=True)

compliedinjected_signal_tau = "injectedsignaltau" + inputarg + ".pkl"  
np.save(compliedinjected_signal_tau, injected_signal_tau, allow_pickle=True)

compliedinjected_signal_amp = "injectedsignalamp" + inputarg + ".pkl"
np.save(compliedinjected_signal_amp, injected_signal_amp, allow_pickle=True)

compliedinjected_signal_optimal_snr = "injectedsignaloptimalsnr" + inputarg + ".pkl"  
np.save(compliedinjected_signal_optimal_snr, injected_signal_optimal_snr, allow_pickle=True)

compliedinjected_signal_RA = "injectedsignalRA" + inputarg + ".pkl"  
np.save(compliedinjected_signal_RA, injected_signal_RA, allow_pickle=True)

compliedinjected_signal_DEC = "injectedsignalDEC" + inputarg + ".pkl"  
np.save(compliedinjected_signal_DEC, injected_signal_DEC, allow_pickle=True)

compliedinjected_signal_inclination = "injectedsignalinclination" + inputarg + ".pkl"     
np.save(compliedinjected_signal_inclination, injected_signal_inclination, allow_pickle=True)
    
    
        
        
        
        
        
        
        
'''        
#########################HISTOGRAM-OF-SNR-NOISE##############################        



xsorted = np.sort(maximum_noise_snr)
binrange = int((xsorted[-1] - xsorted[0])/0.1)
value = int(len(xsorted)*0.99)
threshold = xsorted[value]
print('1% Threshold is values above:',threshold)

# the histogram of the data
n, bins, patches = plt.hist(x, binrange, density=True, facecolor='red', alpha=0.75)
plt.xlabel('snr')
plt.ylabel('freqnecy density')
plt.title('Histogram of SNR')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.xlim(40, 160)
#plt.ylim(0, 0.03)
plt.grid(True)
plt.show()
plt.savefig('SNRHistogramofNoise')

'''





###############################################################################
        
'''      
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
'''


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