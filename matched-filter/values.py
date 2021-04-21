import numpy as np 

from ringdown import RingdownTemplateBank #from templates.py

tb = RingdownTemplateBank(frange=[1000,1001], taurange=[0.05,0.06]) 
#tb = RingdownTemplateBank(frange=[1000,1001], taurange=[0.05,0.06])

print(len(tb)) 
i = 0
for waveform in tb.generate_waveforms(domain="frequency"):  
    print(waveform)
    print(tb[i])
    i += 1
    hp, hc = waveform
    print(hp)
    #hp.get_sample_frequencies().data 
    
print("done")