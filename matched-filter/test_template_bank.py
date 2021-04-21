"""
Show how to create a template bank equivalent to that in Fig. 7.5 (p. 78) of
arXiv:0908.2085.
"""

from ringdown import RingdownTemplateBank
from matplotlib import pyplot as pl


frange = [1230, 1240]  # frequency range (Hz) adapt for neutron stars and then the range of q/tau, realistics values should give thousand tmplates, maybe more
#qrange = [2, 20]  # Quality factor ranges, where quality factor Q is a dimensionless parameter that describes how underdamped an oscillator or resonator is. It is defined as the ratio of the peak energy stored in the resonator in a cycle of oscillation to the energy lost per radian of the cycle. Q factor is alternatively defined as the ratio of a resonator's centre frequency to its bandwidth when subject to an oscillating driving force. These two definitions give numerically similar, but not identical, results. Higher Q indicates a lower rate of energy loss and the oscillations die out more slowly 
mm = 0.03  # maximum mismatch, this means the data signal within these q ranges in its real paramater space, it should match up with the template 97% of the time (1-0.03) don't change
taurange = [0.06,0.07]

tb = RingdownTemplateBank(frange, taurange=taurange, mm=mm)

print("Number of templates is {}".format(len(tb)))

fig, ax = pl.subplots()
ax.semilogx(tb.bank_freqs, tb.bank_qs, '.', color="b", ls="None")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Q")
ax.grid(True, which="both", linestyle="dotted")
pl.show()
