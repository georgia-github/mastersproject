#!/usr/bin/env python
import ringdown
import pycbc.filter
import numpy as np
from matplotlib import pyplot as plt


#9001200
#12001800
#18002400


minf = str(900)
maxf = str(1200)

maximum_snr_of_template = np.load("maximum_snr_of_template" + minf +"to"+ maxf + ".pkl.npy")
maximum_snr_of_chunk = np.load("maximum_snr_of_chunk" + minf +"to"+ maxf + ".pkl.npy")
template_freq = np.load("template_freq" + minf +"to"+ maxf + ".pkl.npy")
#template_tau = np.load("template_tau" + minf +"to"+ maxf + ".pkl.npy")
#template_qs = np.load("template_qs" + minf +"to"+ maxf + ".pkl.npy")
#frange = np.load("frange" + minf + maxf + ".pkl.npy")






################### TEMPLATE FREQUENCY AGAINST SNR FOR ALL TIME CHUNKS #####################

'''
plt.figure()
for i in range(len(maximum_snr_of_template)):
    x1 = template_freq[0]
    y1 = maximum_snr_of_template[i]
    
    x2,y2 = zip(*sorted(zip(x1,y1),key=lambda x1: x1[0]))
    plt.plot(x2, y2)
plt.xlabel('Frequency of Template')
plt.ylabel('Maximum SNR for each \n 2 second data chunk')
plt.title('Measured Maximum Template SNR for each 2 \n second chunk of data over the full 128 seconds')
plt.show()
plt.savefig('multiplefreqsnrplot'+minf+maxf+'.png')    
'''
########################################################################



#############PLOTTING TEMPLATE FREQUENCY AGAINST MAXIMUM SNR FROM ALL DATA CHUNKS INTO ONE FINAL VALUE #####
plt.figure()
maximumsnroverall = []
ydata = maximum_snr_of_template

for x in range(len(template_freq[0])):
    totaly = []
    for i in range(len(ydata)):
        totaly.append(ydata[i][x])
    maximumsnroverall.append(np.amax(totaly))

average_value = np.mean(maximumsnroverall,axis=0)
double_average_value = int(average_value*2)

abnormal_snr = []
abnormal_freq = []

for a in range(len(maximumsnroverall)):
    if maximumsnroverall[a] > double_average_value:
        abnormal_snr.append(maximumsnroverall[a])
        abnormal_freq.append(template_freq[0][a])
        
print(abnormal_snr)        
print(abnormal_freq)



badsignals = "abnormalfrequencies" + minf + "to" + maxf + ".pkl"  
np.save(badsignals,abnormal_freq,allow_pickle=True)  

x3 = template_freq[0]
y3 = maximumsnroverall

x4,y4 = zip(*sorted(zip(x3,y3),key=lambda x3: x3[0]))
plt.plot(x4,y4)    
plt.xlabel('Frequency of Template')
plt.ylabel('Maximum SNR')
plt.title('Measured Maximum Template SNR for the the full 128 seconds')
plt.show()
plt.savefig('overallfreqsnrplot'+minf+maxf+'.png')  

totals = "total_max_snr_" + minf + "to" + maxf + ".pkl"  
np.save(totals,y4,allow_pickle=True)
totalfreqs = "total_max_freqs_" + minf + "to" + maxf + ".pkl"  
np.save(totalfreqs,x4,allow_pickle=True)
######################################################################################






