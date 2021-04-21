import ringdown
import pycbc.filter
import numpy as np
from matplotlib import pyplot as plt

from test_matched_filter_noise_snr import maximum_noise_snr100

print(maximum_noise_snr100)

xsorted = np.sort(maximum_noise_snr100)
binrange = int(((xsorted[-1] - xsorted[0])/0.1)*1.5)
value = int(len(xsorted)*0.99)
threshold = xsorted[value]
#print('1% Threshold is values above:',threshold)
#print(xsorted[-1])
#print(xsorted[0])
#print('There are:',binrange,'bins in this histogram of',len(xsorted),'noise measurements.')


text = 'The 1% threshold is values above:\n{th}\nThere are {b} bins in this histogram \nof {l} noise measurements.'.format(th=threshold,b=binrange,l=len(xsorted))

#the histogram of the data
n, bins, patches = plt.hist(xsorted, binrange, density=True, facecolor='red', alpha=0.75)
plt.xlabel('SNR of Background Noise')
plt.ylabel('Frequency density')
plt.title('Histogram of SNR of Background Noise')
plt.text(5.44,1.4,text,ha='left',wrap=True)
#plt.text(r'1% Threshold is values above:'threshold')
#plt.xlim(40, 160)
#plt.ylim(0, 0.03)
#plt.grid(True)
plt.show()
plt.savefig('SNRHistogramofNoise.png')



         
         

# the cumulative histogram of the data
n, bins, patches = plt.hist(xsorted, binrange, density=True, facecolor='red', alpha=0.75,cumulative=True)
plt.xlabel('SNR of Background Noise')
plt.ylabel('Frequency Density')
plt.title('Cumulative Histogram of SNR of Background Noise ')
#plt.text(r'1% Threshold is values above:'threshold')
#plt.xlim(40, 160)
#plt.ylim(0, 0.03)
#plt.grid(True)
plt.show()
plt.savefig('SNRCumulativeHistogramofNoise.png')
