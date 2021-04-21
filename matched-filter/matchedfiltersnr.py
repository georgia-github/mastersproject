import pycbc.noise
import pycbc.psd
import pycbc.filter
import pycbc.waveform
import pylab
from ringdown import RingdownTemplateBank 

     
    
    
tb = RingdownTemplateBank(frange=[1000,3000], taurange=[0.05,0.4]) 
#tb = RingdownTemplateBank(frange=[1000,1001], taurange=[0.05,0.06])

for waveform in tb.generate_waveforms(domain="frequency"): 
       hp, hc = waveform

#stilde.resize(len(hp))


hpt = hp.to_timeseries()
delta_t = hpt.delta_t
print(hpt.delta_t)

# Generate some noise with an advanced ligo psd
flow = 20.0
delta_f = hp.delta_f
flen = int(hp.sample_rate / delta_f) + 1
psd = pycbc.psd.aLIGOZeroDetHighPower(flen, delta_f, flow)

# Generate 16 seconds of noise at 4096 Hz
#delta_t = 1.0 / 4096
tsamples = len(hp)
strain = pycbc.noise.noise_from_psd(tsamples, delta_t, psd, seed=127)
stilde = strain.to_frequencyseries()
hp.resize(len(stilde))


snr = pycbc.filter.matched_filter(hp, stilde, psd, low_frequency_cutoff=flow, high_frequency_cutoff=None, sigmasq=None)
print(snr.psd)

pylab.plot(snr.sample_times, abs(snr),color='royalblue')
pylab.ylabel('Signal-to-Noise Ratio')
pylab.title('Matched Filter run on generated noise')
pylab.xlabel('Time (s)')
pylab.show()