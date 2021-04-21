import bilby
from bilby.core.result import read_in_result
from matplotlib import pyplot as plt
import numpy as np

myresfile = "PSR_B0833-45_result.json"  
res = read_in_result(myresfile)

plt.figure()
ul = np.quantile(res.posterior["amplitude"], 0.9)
#res.plot_corner(parameters=["amplitude"], color="r")
#ax = kwargs.get("ax", plt.subplot())
ax = plt.gca()
ax.set_ylabel("Amplitude $h_{0}$")
ax.set_xlabel('Amplitude')

fig = res.plot_corner(parameters=["amplitude"], color="r", save=False,label='Data')
ax.axvline(ul, color="r", linestyle="--",label='Upper Limit')
#ax.legend()
fig.savefig("myfig.png", dpi=300)


#res.plot_single_density(key='amplitude',file_base_name='PSR_B0833-45_result',color='r')



print("The 90% credible upper limit on h0 is {0:.2e}".format(ul))

#plt.savefig('amplitude.pdf')