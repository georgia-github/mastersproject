"""
Show how to create a time-domain signal.
"""

from matplotlib import pyplot as plt
from pycbc.waveform import ringdown_td_approximants


params = dict(
    lmns="221",
    tau_220=0.5,
    f_220=1234.0,
    amp220=1e-21,
    phi220=0.3,
    inclination=0.2,
    polarization=1.1,
    t_final=2.0,
)

# plot waveform
hp, hc = ringdown_td_approximants["TdQNMfromFreqTau"](
    f_lower=20,
    delta_t=1.0/2048,
    **params,
)


plt.figure()
plt.title('A Simulated Ring-down Signal Waveform')
plt.plot(hp.sample_times, hp,color='lightskyblue',linewidth=0.1)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
plt.savefig('InjectedSignalParams.png')

plt.figure()

# plot frequency domain
hf = hp.to_frequencyseries()
plt.semilogx(hf.sample_frequencies, hf.real(),color='lightskyblue')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Injected Signal Frequency compared to \nthe range of Sample Frequencies')
plt.show()
plt.savefig('InjectedSignal.png')
