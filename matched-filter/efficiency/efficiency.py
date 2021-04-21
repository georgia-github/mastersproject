import numpy as np
import pycbc.filter
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

maximum_noise_snr100 = np.load("compliednoisedatasnr.pkl.npy")
maximum_noise_snrsignals = np.load("complied2maximum_noise_snrsignals.pkl.npy")
injected_signal_optimal_snr = np.load("complied2injected_signal_optimal_snr.pkl.npy")

x = 9

injected_signal_optimal_snr = injected_signal_optimal_snr[maximum_noise_snrsignals < x]
maximum_noise_snrsignals = maximum_noise_snrsignals[maximum_noise_snrsignals < x]

snrs = injected_signal_optimal_snr
snrs2 = maximum_noise_snrsignals

maximum_noise_snr = np.array(maximum_noise_snr100)
xsorted = np.sort(maximum_noise_snr)
value = int(len(xsorted)*0.999)
threshold = xsorted[value]

# set the histogram bins edges that you want to use
# (let's say from the lowest to largest SNRs in steps of 2)
step = 0.04
bins = np.arange(np.floor(np.min(snrs)), np.ceil(np.max(snrs)) + step, step)
# histogram the data to get the number of SNRs in each bin
nperbin, _ = np.histogram(snrs, bins=bins)
# now do the same with the thresholded data (but using the same bins as before)
nabovethresh, _ = np.histogram(snrs2[snrs > threshold], bins=bins)



newbins = []
newnabovethresh = []
newnperbin = []

for i in range(len(nperbin)):
    if nperbin[i] != 0:
        newnperbin.append(nperbin[i])
        newbins.append(bins[i])
        newnabovethresh.append(nabovethresh[i])

# efficiency will then be...
efficiency = np.divide(newnabovethresh,newnperbin)

curve = np.polyfit(newbins, efficiency, 4)
polynomial = np.poly1d(curve)

polyplot = []
for i in newbins:
    polyplot.append(polynomial(i))
    
    
ydata = efficiency
xdata = newbins
    
    
def sigmoid(x, L ,x0, k, b):
    y = L / (1 + np.exp(-k*(x-x0)))+b
    return (y)

p0 = [max(ydata), np.median(xdata),1,min(ydata)] # this is an mandatory initial guess

popt, pcov = curve_fit(sigmoid, xdata, ydata,p0, method='dogbox',maxfev=10000)
    
    
    
from scipy import stats
import numpy as np
from scipy.optimize import minimize
import pylab as py



def sigmoid(params):
    k = params[0]
    x0 = params[1]   
    sd = params[2]

    yPred = 1 / (1+ np.exp(-k*(xdata-x0)))

    # Calculate negative log likelihood
    LL = -np.sum( stats.norm.logpdf(efficiency, loc=yPred, scale=sd ) )

    return(LL)


initParams = [1, 1, 1]

results = minimize(sigmoid, initParams, method='Nelder-Mead')


estParms = results.x
yOut = yPred = 1 / (1+ np.exp(-estParms[0]*(newbins-estParms[1])))

#snrbinplotvalues = newbins[yOut > 0.999]
#efficiencyvalues = y0ut[yOut > 0.999]
#print(yOut[-2])
#print(newbins[-2])

#print('The 0.01\% threshold value at',snrbinplotvalues[0],'occurs for SNR value:',efficiencyvalues[0])
for i in range(len(newbins)):
    x = newbins[i]
    if x==6.640000000000001:
        print(i)
        print('the 0.1%threshold of',threshold,'has efficiency',yOut[i])   
    else:
        i+=1
#print('done')

#print(newbins)

print(threshold)



plt.figure()   
plt.plot(newbins, yOut, marker='.', color='royalblue',label='Generated Data for \nthe 0.1% Threshold')      
plt.title('Efficiency of the Matched Filter',loc='center')
plt.plot([threshold,threshold],[-0.1,1.1],linestyle='dotted',color='royalblue',label='0.1% Threshold Value')





value2 = int(len(xsorted)*0.99)
threshold2 = xsorted[value2]

nabovethresh2, _ = np.histogram(snrs2[snrs > threshold2], bins=bins)


newbins2 = []
newnabovethresh2 = []
newnperbin2 = []

for i in range(len(nperbin)):
    if nperbin[i] != 0:
        newnperbin2.append(nperbin[i])
        newbins2.append(bins[i])
        newnabovethresh2.append(nabovethresh2[i])

efficiency2 = np.divide(newnabovethresh2,newnperbin2)

ydata2 = efficiency2
xdata2 = newbins2

def sigmoid(x, L ,x0, k, b):
    y = L / (1 + np.exp(-k*(x-x0)))+b
    return (y)

p02 = [max(ydata2), np.median(xdata2),1,min(ydata2)] # this is an mandatory initial guess

popt, pcov = curve_fit(sigmoid, xdata2, ydata2,p02, method='dogbox',maxfev=10000)


def sigmoid(params):
    k = params[0]
    x0 = params[1]   
    sd = params[2]

    yPred = 1 / (1+ np.exp(-k*(xdata2-x0)))

    # Calculate negative log likelihood
    LL = -np.sum( stats.norm.logpdf(efficiency2, loc=yPred, scale=sd ) )

    return(LL)


initParams2 = [1, 1, 1]

results2 = minimize(sigmoid, initParams2, method='Nelder-Mead')


estParms2 = results2.x
yOut2 = yPred = 1 / (1+ np.exp(-estParms2[0]*(newbins2-estParms2[1])))

plt.plot(newbins2, yOut2, marker='.', color='skyblue',label='Generated Data for \nthe 1% Threshold')      
plt.plot([threshold2,threshold2],[-0.1,1.1],linestyle='dotted',color='skyblue',label='1% Threshold Value')



plt.legend()
plt.xlabel('SNR Value of Signal')
plt.ylabel('Efficiency of Detection')

y = threshold2
#print(y)
#6.179
#newbins3 = newbins2[newbins2 > y]
#print(threshold2)
#print(newbins2)
#print(newbins3)

for i in range(len(newbins2)):
    x = newbins2[i]
    if x==6.2:
        print('the 1%threshold of',threshold2,'has efficiency',yOut2[i])
    else:
        i+=1




plt.show()
plt.savefig('newefficiency.png')


