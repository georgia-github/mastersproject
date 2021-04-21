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
 


gwfreqsuncut = np.load('gwdatatotalfreqs.npy')
gwsnrsuncut = np.load('gwdatatotalsnrs.npy')

gwfreqscut = []
gwsnrscut = []

cutrange4 = [0,1300]
cutrange5 = [2400,3000]
cutrange6 = [0,0]

for i in range(len(gwfreqsuncut)):
    if (cutrange4[0] <= gwfreqsuncut[i] <= cutrange4[1]) or (cutrange5[0] <= gwfreqsuncut[i] <= cutrange5[1]) or (cutrange6[0] <= gwfreqsuncut[i] <= cutrange6[1]) :
        continue
    else:
        gwsnrscut.append(gwsnrsuncut[i])
        gwfreqscut.append(gwfreqsuncut[i])


        
        
plt.figure()        
        
x11 = gwfreqscut
y11 = gwsnrscut
x21,y21 = zip(*sorted(zip(x11,y11),key=lambda x11: x11[0]))
plt.plot(x21,y21,label='H1 GW170817 \nOff-Source Strain Data',alpha=0.7,linewidth=1,color='green')  

#B0833-45 	PSR0835-4510
#he Vela Pulsar (PSR J0835-4510 or PSR B0833-45)

x5 = np.load('totalfreqsrangeuncut.pkl.npy')
y5 = np.load('totalsnrsuncutforalldata.pkl.npy')
x6,y6 = zip(*sorted(zip(x5,y5),key=lambda x5: x5[0]))
plt.plot(x6,y6,label='H1 PSR J0835-451 \nOff-Source Strain Data',alpha=0.7,linewidth=2,color='blue')  

x1 = total_frequencies
y1 = total_snrs
x2,y2 = zip(*sorted(zip(x1,y1),key=lambda x1: x1[0]))
plt.plot(x2,y2,label='H1 PSRJ0835-451 \nOn-Source Strain Data',alpha=0.7,linewidth=1,color='red') 



plt.xlabel('Frequency of Template (Hz)')
plt.ylabel('Maximum SNR')
plt.title('Measured Maximum Template SNR of 3 H1 Strain Data Sets')

#plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.15), ncol=3, fancybox=True)
plt.legend(loc="upper right")
plt.show()
plt.savefig('overlappingplotuncutwithgw'+inputarg+'.png',bbox_inches='tight')  

######################################################################################


#############PLOTTING TEMPLATE FREQUENCY AGAINST MAXIMUM SNR FROM ALL DATA CHUNKS INTO ONE FINAL VALUE #####
plt.figure()
x7 = np.load('totalfreqsrange.pkl.npy')
y7 = np.load('totalsnrsforalldata.pkl.npy')
x8,y8 = zip(*sorted(zip(x7,y7),key=lambda x7: x7[0]))
plt.plot(x8,y8,label='H1 PSR J0835-451 Off-Source Strain Data',alpha=0.7,linewidth=2,color='blue')  


x3 = cut_total_frequencies
y3 = cut_total_snrs
x4,y4 = zip(*sorted(zip(x3,y3),key=lambda x3: x3[0]))
plt.plot(x4,y4,label='H1 PSR J0835-451 On-Source Strain Data',alpha=0.9,linewidth=1,color='red')   

 

#text = 'There are frequency cuts from {a} and {b} Hz'.format(a=cutrange1,b=cutrange2)
#plt.text(1200,2.4,text,ha='left',wrap=True)

#plt.plot([1300,2400],[6.95541347,6.95541347],label='1% Threshold',color='red')
#plt.plot([1300,2400],[8.093896679,8.093896679],label='0.1% Threshold',color='black')

plt.xlabel('Frequency of Template (Hz)')
plt.ylabel('Maximum SNR')
plt.title('Measured Maximum Template SNR for the Strain Data \nof the 2016 PSR J0835-451 Glitch')
#, after frequency cuts at\n 1452-1495Hz and 2010-2020Hz
#plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.15), ncol=3, fancybox=True)
plt.legend(loc="upper right")
plt.show()
plt.savefig('overlappingplotcutnewcolors'+inputarg+'.png',bbox_inches='tight')  



















