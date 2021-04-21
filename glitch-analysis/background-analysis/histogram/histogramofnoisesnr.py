import ringdown
import pycbc.filter
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.distributions.mixture_rvs import mixture_rvs

totalsnrsforalldata = np.load('totalsnrsforalldata.pkl.npy')

totalnoisedata = totalsnrsforalldata

xsorted = np.sort(totalnoisedata)
binrange = int(((xsorted[-1] - xsorted[0])/0.1)*1.5)
value99 = int(len(xsorted)*0.99)
threshold99 = xsorted[value99]
value999 = int(len(xsorted)*0.999)
threshold999 = xsorted[value999]


#print('1% Threshold is values above:',threshold)
#print(xsorted[-1])
#print(xsorted[0])
#print('There are:',binrange,'bins in this histogram of',len(xsorted),'noise measurements.')


text = 'The 1% threshold is values above:{th99}\nThe 0.1% threshold is values above:{th999}\nThere are {b} bins in this histogram of {l} noise measurements.\n There are 623 segments of 128 second chunks of background data \n taken 1 day before the 2016 Vela Pulsar Glitch at 1165577780GPS.'.format(th99=threshold99,th999=threshold999,b=binrange,l=len(xsorted))

#the histogram of the data
plt.figure()
n, bins, patches = plt.hist(xsorted, binrange, density=True, facecolor='red', alpha=0.75,label='Background Noise Data')
plt.xlabel('SNR of Background Noise')
plt.ylabel('Frequency density')
plt.title('Histogram of SNR Values of Off-Source Strain \nData from the 2016 PSR J0835-451 Glitch')
#plt.text(2.9,-0.4,text,ha='left',wrap=True)
#plt.text(r'1% Threshold is values above:'threshold')
#plt.xlim(40, 160)
#plt.ylim(0, 0.03)
#plt.grid(True)

kde = sm.nonparametric.KDEUnivariate(xsorted)
kde.fit() # Estimate the densities
plt.plot(kde.support, kde.density, lw=3, label='Gaussian Fitted \n Estimation', zorder=10, color='black')

plt.legend()

plt.show()
plt.savefig('SNRHistogramofNoise.png',bbox_inches='tight')



         
'''         
plt.figure()
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
plt.savefig('SNRCumulativeHistogramofNoise.png',bbox_inches='tight')
'''

