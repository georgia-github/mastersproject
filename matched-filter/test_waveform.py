"""
Show how to create a time-domain signal.
"""

from matplotlib import pyplot as pl
from pycbc.waveform import ringdown_td_approximants


params = dict(
    lmns="221", # quasi normal modes, always stick with 221
    tau_220=0.06, # rindgodwn decay frequency / tau
    f_220=1600.0,
    amp220=1e-22,
    phi220=0.3,
    inclination=0.2,
    polarization=1.1,
    t_final=2.0, # duration of waveform
)

# plot waveform
hp, hc = ringdown_td_approximants["TdQNMfromFreqTau"](
    f_lower=1000,
    delta_t=1.0/4096,
    **params,
)

fig, ax = pl.subplots(2, 1, figsize=(5, 9))
ax[0].plot(hp.sample_times, hp)
ax[0].set_xlabel("Time (s)")
ax[0].set_ylabel("Amplitude")

# plot frequency domain
hf = hp.to_frequencyseries()
ax[1].semilogx(hf.sample_frequencies, hf.real())
ax[1].set_xlabel('Frequency (Hz)')

fig.tight_layout()
pl.show()
