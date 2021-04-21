import ringdown
import pycbc.filter
import numpy as np
from gwpy.timeseries import TimeSeries
from pycbc.types.timeseries import TimeSeries as PyCBCTimeSeries
from pycbc.psd import interpolate
from matplotlib import pyplot as plt


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
