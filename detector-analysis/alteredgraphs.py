import ringdown
import pycbc.filter
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import cm

maxsnrs = []

maximum_snr_of_template1 = np.load("maximum_snr_of_template1800to2400.pkl.npy")
template_freq1 = np.load("template_freq1800to2400.pkl.npy")

maximum_snr_of_template2 = np.load("maximum_snr_of_template900to1200.pkl.npy")
template_freq2 = np.load("template_freq900to1200.pkl.npy")

maximum_snr_of_template3 = np.load("maximum_snr_of_template1200to1800.pkl.npy")
template_freq3 = np.load("template_freq1200to1800.pkl.npy")

freqs = []

maxsnrs.append(maximum_snr_of_template1)
maxsnrs.append(maximum_snr_of_template2)
maxsnrs.append(maximum_snr_of_template3)

freqs.append(template_freq1)
freqs.append(template_freq2)
freqs.append(template_freq3)

#print(len(maxsnrs))
#print(len(freqs))
#print(template_freq2)
#print(maximum_snr_of_chunk1)
'''
cutrange1 = [1210,1220]
cutrange2 = [1280,1290]

for i in range(len(template_freq1)):
    if (cutrange1[0] <= template_freq2[i] <= cutrange1[1]) or (cutrange2[0] <= template_freq2[i] <= cutrange2[1]) :
        continue
    else:
        maximum_snr_of_template.append(maximum_snr_of_template1[0][i])
        #maximum_snr_of_chunk.append(maximum_snr_of_chunk1[][i])
        template_freq.append(template_freq1[0][i])


#print(len(template_freq))
#print((maximum_snr_of_template))
'''



'''
for i in range(len(maxsnrs)):
    x11 = freqs[i]
    y11 = maxsnrs[i]
   
    x21,y21 = zip(*sorted(zip(x11,y11),key=lambda x11: x11[0]))
    plt.plot(x21, y21)

#plt.plot(maxsnrs,freqs)    
plt.xlabel('Frequency of Template')
plt.ylabel('Maximum SNR')
plt.title('Measured Maximum Template SNR for each 2s \n chunk of data over 128s')
plt.show()
plt.savefig('multiplefreqsnrplotall.png')    
'''



################### TEMPLATE FREQUENCY AGAINST SNR FOR ALL TIME CHUNKS #####################


plt.figure()

color=iter(cm.tab10(np.linspace(0,1,61)))



for i in range(len(maximum_snr_of_template1)):
    c=next(color)
    x1 = template_freq1[i]
    y1 = maximum_snr_of_template1[i]
    
    x2,y2 = zip(*sorted(zip(x1,y1),key=lambda x1: x1[0]))
    plt.plot(x2, y2,color=c,alpha=0.7)
    

    x3 = template_freq2[i]
    y3 = maximum_snr_of_template2[i]
    
    x4,y4 = zip(*sorted(zip(x3,y3),key=lambda x3: x3[0]))
    plt.plot(x4, y4,color=c,alpha=0.7)
    

    x5 = template_freq3[i]
    y5 = maximum_snr_of_template3[i]
    
    x6,y6 = zip(*sorted(zip(x5,y5),key=lambda x5: x5[0]))
    plt.plot(x6, y6,color=c,alpha=0.7)
    

plt.xlabel('Frequency of Template (Hz)')
plt.ylabel('Maximum SNR')
plt.title('Measured Maximum Template SNR for each 2 second Segment of \nOff-Source Gravitational-Wave Strain Data from GW170817')
plt.show()
plt.savefig('multiplefreqsnrplotall.png')    

########################################################################
'''
for i in range(len(maximum_snr_of_template1)):
    x1 = template_freq1[i]
    y1 = maximum_snr_of_template1[i]
    
    x2,y2 = zip(*sorted(zip(x1,y1),key=lambda x1: x1[0]))
    #plt.plot(x2, y2)
    
for i in range(len(maximum_snr_of_template2)):
    x3 = template_freq2[i]
    y3 = maximum_snr_of_template2[i]
    
    x4,y4 = zip(*sorted(zip(x3,y3),key=lambda x3: x3[0]))
    #plt.plot(x4, y4)
    
for i in range(len(maximum_snr_of_template3)):
    x5 = template_freq3[i]
    y5 = maximum_snr_of_template3[i]
    
    x6,y6 = zip(*sorted(zip(x5,y5),key=lambda x5: x5[0]))
    #plt.plot(x6, y6)
'''
