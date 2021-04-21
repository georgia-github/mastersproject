import ringdown
import pycbc.filter
import numpy as np
from matplotlib import pyplot as plt



maximum_noise_snr100 = np.load("compliednoisedatasnr.pkl.npy")
maximum_noise_snrsignals = np.load("compliedmaximum_noise_snrsignals.pkl.npy")
injected_signal_freq = np.load("compliedinjected_signal_freq.pkl.npy")
injected_signal_tau = np.load("compliedinjected_signal_tau.pkl.npy")
injected_signal_amp = np.load("compliedinjected_signal_amp.pkl.npy")
injected_signal_optimal_snr = np.load("compliedinjected_signal_optimal_snr.pkl.npy")
injected_signal_RA = np.load("compliedinjected_signal_RA.pkl.npy")
injected_signal_DEC = np.load("compliedinjected_signal_DEC.pkl.npy")
injected_signal_inclination = np.load("compliedinjected_signal_inclination.pkl.npy")

print(maximum_noise_snrsignals)

maximum_noise_snr = np.array(maximum_noise_snr100)
xsorted = np.sort(maximum_noise_snr)
value = int(len(xsorted)*0.999)
threshold = xsorted[value]



maximum_noise_snrsignals = np.array(maximum_noise_snrsignals)
injected_signal_optimal_snr = np.array(injected_signal_optimal_snr)
injected_signal_freq = np.array(injected_signal_freq)
injected_signal_tau = np.array(injected_signal_tau)
injected_signal_amp = np.array(injected_signal_amp)
injected_signal_RA = np.array(injected_signal_RA)
injected_signal_DEC = np.array(injected_signal_DEC)
injected_signal_inclination = np.array(injected_signal_inclination)

'''
injected_signal_optimal_snr = injected_signal_optimal_snr[maximum_noise_snrsignals > threshold]
injected_signal_freq = injected_signal_freq[maximum_noise_snrsignals > threshold]
injected_signal_tau = injected_signal_tau[maximum_noise_snrsignals > threshold]
injected_signal_amp = injected_signal_amp[maximum_noise_snrsignals > threshold]
injected_signal_RA = injected_signal_RA[maximum_noise_snrsignals > threshold]
injected_signal_DEC = injected_signal_DEC[maximum_noise_snrsignals > threshold]
injected_signal_inclination = injected_signal_inclination[maximum_noise_snrsignals > threshold]
maximum_noise_snrsignals = maximum_noise_snrsignals[maximum_noise_snrsignals > threshold]
# scatter graph 
'''
print(maximum_noise_snrsignals)
print(threshold)




#####################PLOTTING-MAXIMUM-SNR-AGAINST-OPTIMAL-SNR##############################
xplot1 = injected_signal_optimal_snr
yplot1 = maximum_noise_snrsignals
plt.scatter(xplot1, yplot1)
plt.xlabel('Injected Signal Optimal SNR')
plt.ylabel('Measured Signal SNR')
plt.title('Injected Randomly Generated Ringdown Signals')
plt.show()
plt.savefig('InjectedSignalSNRGraph.png')
############################################################################################


########PLOTTING-INJECTED-FREQUENCY-AGAINST-TAU-WITH-SNR-DETECTION-COLOUR-SCALE#################
xplot2 = injected_signal_freq
yplot2 = injected_signal_tau
area2 = np.divide(maximum_noise_snrsignals,injected_signal_optimal_snr)*20
plt.scatter(xplot2, yplot2,s=area2,c=area2,marker='o',cmap="Blues",edgecolor="black")
cbar = plt.colorbar()
cbar.set_label('Relative Strength of detected SNR to optimal SNR')
plt.xlabel('Injected Signal Frequency')
plt.ylabel('Injected Signal Tau')
plt.title('Injected Randomly Generated Ringdown Signals')
plt.show()
plt.savefig('InjectedSignalSNRFrequencyAgainstTauGraph.png')


#################################################################################################

#########PLOTTING-INJECTED-AMPLITUDE-AGAINST-OPTIMAL-SNR-VAUE-RATIO-TO-DETECTED-SNR-VALUE############
xplot3 = injected_signal_amp
yplot3 = maximum_noise_snrsignals
area3 = np.divide(maximum_noise_snrsignals,injected_signal_optimal_snr)*20
plt.title('Injected Randomly Generated Ringdown Signals',loc='center')
plt.scatter(xplot3, yplot3,s=area3,c=area3,marker='o',cmap='Blues',edgecolor='black')
cbar = plt.colorbar()
cbar.set_label('Relative Strength of detected SNR to optimal SNR')
#plt.legend(['Randomly Generated Ringdown Signals','Measured Signal SNR / Optimal Signal SNR'],loc="upper left")
plt.xlabel('Injected Signal Amplitude')
plt.ylabel('Measured Signal SNR')
plt.show()
plt.savefig('InjectedSignalAmplitudeSNRGraph.png')

#####################################################################################################


#######################EFFICIENCY-OF-ALGORITHM-GRAPH#################################################

# efficiency is percent of signals over threshold at certain snr's so in certain bins i want to know how many were detected above the threshold or how many were detected above their optimal snr detection signal

# 6.4 is usual threshold from 0 to 200 basically
























