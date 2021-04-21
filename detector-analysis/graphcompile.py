#!/usr/bin/env python
import ringdown
import pycbc.filter
import numpy as np
from matplotlib import pyplot as plt

total_frequencies = np.load('totalfreqs900to2400.pkl.npy')
total_snrs = np.load('totalsnrs900to2400.pkl.npy')
'''
freqs9001200 = np.load('total_max_freqs_900to1200.pkl.npy')
snrs9001200 = np.load('total_max_snr_900to1200.pkl.npy')
freqs12001800 = np.load('total_max_freqs_1200to1800.pkl.npy')
snrs12001800 = np.load('total_max_snr_1200to1800.pkl.npy')
freqs18002400 = np.load('total_max_freqs_1800to2400.pkl.npy')
snrs18002400 = np.load('total_max_snr_1800to2400.pkl.npy')



total_frequencies = np.concatenate((total_frequencies, freqs9001200),axis=0)
total_frequencies = np.concatenate((total_frequencies, freqs12001800),axis=0)
total_frequencies = np.concatenate((total_frequencies, freqs18002400),axis=0)


total_snrs = np.concatenate((total_snrs, snrs9001200),axis=0)
total_snrs = np.concatenate((total_snrs, snrs12001800),axis=0)
total_snrs = np.concatenate((total_snrs, snrs18002400),axis=0)




np.save('totalfreqs900to2400.pkl',total_frequencies,allow_pickle=True)
np.save('totalsnrs900to2400.pkl',total_snrs,allow_pickle=True)
'''
plt.figure()
plt.plot(total_frequencies,total_snrs,color='blue')    
plt.xlabel('Frequency of Template')
plt.ylabel('Maximum SNR')
plt.title('Measured Maximum Template SNR for 128s of \nGW170817 Off-Source Data Observed by H1')
plt.show()
plt.savefig('totalcompliedfreqsnr.png')  




#######frequency cutting##############


cut_total_frequencies = np.load('cutfrequencytotalcompile.pkl.npy')
cut_total_snrs = np.load('cutsnrstotalcompile.pkl.npy')

cutrange1 = [1465,1485]
cutrange2 = [1495,1510]
cutrange3 = [900,1000]


'''
for i in range(len(total_frequencies)):
    if (cutrange1[0] <= total_frequencies[i] <= cutrange1[1]) or (cutrange2[0] <= total_frequencies[i] <= cutrange2[1]) or (cutrange3[0] <= total_frequencies[i] <= cutrange3[1]) :
        continue
    else:
        cut_total_snrs.append(total_snrs[i])
        cut_total_frequencies.append(total_frequencies[i])


print(np.amax(total_snrs))
print(len(total_frequencies),len(cut_total_frequencies))

np.save('cutfrequencytotalcompile.pkl',cut_total_frequencies,allow_pickle=True)
np.save('cutsnrstotalcompile.pkl',cut_total_snrs,allow_pickle=True)
'''
plt.figure()
#x1 = cut_total_frequencies
#y1 = cut_total_snrs
    
#x2,y2 = zip(*sorted(zip(x1,y1),key=lambda x1: x1[0]))
#plt.plot(x2, y2)

txt = 'Frequencies have been cut \n from 1465-1485Hz and 1495-1510Hz,\n resulting in {c} total measurements.'.format(c=int(len(cut_total_frequencies)))


plt.xlabel('Frequency of Template')
plt.ylabel('Maximum SNR')
plt.title('Measured Maximum Template SNR for 128s of \nGW170817 Off-Source Data Observed by H1.')
#plt.text(1400,6.4,txt,ha='center')
plt.plot(cut_total_frequencies,cut_total_snrs,color='blue')
plt.show()
plt.savefig('totalcutcompiledfreqsnrs.png')    







