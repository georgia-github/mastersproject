#!/usr/bin/env python
import ringdown
import pycbc.filter
import numpy as np
from matplotlib import pyplot as plt
from gwpy.timeseries import TimeSeries
from pycbc.types.timeseries import TimeSeries as PyCBCTimeSeries
from pycbc.psd import interpolate
import sys


uncutmaximumsnroverall = np.load("totalsnrsuncutforalldata.pkl.npy")
uncuttemplate_freq = np.load("totalfreqsrangeuncut.pkl.npy")


maximumsnroverall = np.load("totalsnrsforalldata.pkl.npy")
template_freq = np.load("totalfreqsrange.pkl.npy")







################### TEMPLATE FREQUENCY AGAINST SNR FOR ALL TIME CHUNKS #####################

plt.figure()

x1 = uncuttemplate_freq
y1 = uncutmaximumsnroverall

x2,y2 = zip(*sorted(zip(x1,y1),key=lambda x1: x1[0]))
plt.plot(x2,y2)    
plt.xlabel('Frequency of Template')
plt.ylabel('Maximum SNR')
plt.title('Measured Maximum Template SNR\'s \nfor the uncut frequency range')
plt.show()
plt.savefig('overallfreqsnrplotuncut.png')  


########################################################################



#########PLOTTING TEMPLATE FREQUENCY AGAINST MAXIMUM SNR FROM ALL DATA CHUNKS INTO ONE FINAL VALUE#####
plt.figure()

x3 = template_freq
y3 = maximumsnroverall

x4,y4 = zip(*sorted(zip(x3,y3),key=lambda x3: x3[0]))
plt.plot(x4,y4)    
plt.xlabel('Frequency of Template')
plt.ylabel('Maximum SNR')
plt.title('Measured Maximum Template SNR\'s \nfor the cut frequency range')
plt.show()
plt.savefig('overallfreqsnrplot.png')  

######################################################################################

'''

############# ACTUAL TIME DATA PLOT OF STRAIN #########
plt.figure()
data = np.load('fulldatasetnoise.pkl.npy')
plt.plot(data)
plt.title('LIGO Livingston Observatory data')
plt.ylabel('Strain amplitude')
plt.xlabel('GPS Time')
plt.show()
plt.savefig('overalldataplot.png')

########################################################


'''