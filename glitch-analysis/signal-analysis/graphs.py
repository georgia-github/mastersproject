#!/usr/bin/env python
import ringdown
import pycbc.filter
import numpy as np
from matplotlib import pyplot as plt


inputarg = 'run1'

#template_freq = np.load('signaltotalfreqscut' + inputarg + ".pkl.npy")
#maximum_snr_of_chunk = np.load('signaltotalsnrscut' + inputarg + ".pkl.npy")

total_frequencies = np.load('signaltotalfreqsuncut' + inputarg + ".pkl.npy")
total_snrs = np.load('signaltotalsnrsuncut' + inputarg + ".pkl.npy")

cut_total_frequencies = []
cut_total_snrs = []

cutrange1 = [1452,1495]
cutrange2 = [2010,2020]
cutrange3 = [0,0]

for i in range(len(total_frequencies)):
    if (cutrange1[0] <= total_frequencies[i] <= cutrange1[1]) or (cutrange2[0] <= total_frequencies[i] <= cutrange2[1]) or (cutrange3[0] <= total_frequencies[i] <= cutrange3[1]) :
        continue
    else:
        cut_total_snrs.append(total_snrs[i])
        cut_total_frequencies.append(total_frequencies[i])

#############PLOTTING TEMPLATE FREQUENCY AGAINST MAXIMUM SNR FROM ALL DATA CHUNKS INTO ONE FINAL VALUE #####
plt.figure()


x3 = cut_total_frequencies
y3 = cut_total_snrs

text = 'There are frequency cuts from {a} and {b} Hz'.format(a=cutrange1,b=cutrange2)

x4,y4 = zip(*sorted(zip(x3,y3),key=lambda x3: x3[0]))
plt.plot(x4,y4,label='H1 PSR J0835-451 On-Source Data',color='red')    
plt.plot([1300,2400],[6.95541347,6.95541347],label='1% Threshold',color='black',linestyle='dotted')
plt.plot([1300,2400],[8.093896679,8.093896679],label='0.1% Threshold',color='black',linestyle='dashed')
plt.xlabel('Frequency of Template (Hz)')
plt.ylabel('Maximum SNR')
plt.title('Measured Maximum Template SNR for the On-Source \nStrain Data of the 2016 PSR J0835-451 Glitch')
plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.15), ncol=3, fancybox=True)
#plt.text(1200,2.4,text,ha='left',wrap=True)
plt.show()
plt.savefig('overallfreqsnrplotwithouttext'+inputarg+'.png',bbox_inches='tight')  

print('The highest SNR Values of ',np.amax(y4),'occurs at a frequency of',x4[np.argmax(y4)],'Hz')


######################################################################################



















