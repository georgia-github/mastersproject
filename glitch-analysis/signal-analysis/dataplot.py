import ringdown
import pycbc.filter
import numpy as np
from gwpy.timeseries import TimeSeries
from pycbc.types.timeseries import TimeSeries as PyCBCTimeSeries
from pycbc.psd import interpolate
from matplotlib import pyplot as plt


glitchtime = 1165577780
addedtime = 128
gpsstart = glitchtime - addedtime
gpsend = glitchtime + addedtime
duration = (addedtime*2)
samplerate = 16384 
detector = "H1"

data = TimeSeries.fetch_open_data(
        detector,
        gpsstart,
        gpsend,
        sample_rate=samplerate,
        format='hdf5',
        host='https://www.gw-openscience.org',
        verbose=False,
        cache=True,
)
    
    
lowcutoff = 1000
highcutoff = 3000
buffer = 50  # just allow a bit of a buffer at the edges
filtereddata = data.bandpass(lowcutoff - buffer, highcutoff + buffer)
    
    

    

#np.save('fulldatasetglitch.pkl',filtereddata,allow_pickle=True)
print(len(filtereddata))


############# ACTUAL TIME DATA PLOT OF STRAIN #########
plt.figure()
plt.plot(data,label='Unfiltered Detector Data',color='blue')
plt.plot(filtereddata,label='Detector Data filtered between 1000-3000Hz',color='red')
plt.legend()
plt.title('aLIGO H1 Observed Gravitational-Wave Strain On-Source\n Data of the 2016 PSR J0835-451 Glitch')
plt.ylabel('Strain Amplitude')
plt.xlabel('GPS Time')
plt.tight_layout()
plt.show()
plt.savefig('glitchdataplot.png', bbox_inches = "tight")

########################################################