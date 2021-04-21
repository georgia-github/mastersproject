import numpy as np
from pathlib import Path


maximum_noise_snrsignals = []
injected_signal_freq = []
injected_signal_tau = []
injected_signal_amp = []
injected_signal_optimal_snr = []
injected_signal_RA = []
injected_signal_DEC = []
injected_signal_inclination = []





for i in range(1000):
    file_name = Path('maximumsnrsignal{}.pkl.npy'.format(i))
    if file_name.exists():
        maximum_noise_snrsignals = np.concatenate((maximum_noise_snrsignals, np.load('maximumsnrsignal{}.pkl.npy'.format(i))),axis=0)
        injected_signal_freq = np.concatenate((injected_signal_freq, np.load('injectedsignalfreq{}.pkl.npy'.format(i),allow_pickle=True)),axis=0)
        injected_signal_tau = np.concatenate((injected_signal_tau, np.load('injectedsignaltau{}.pkl.npy'.format(i),allow_pickle=True)),axis=0)
        injected_signal_amp = np.concatenate((injected_signal_amp, np.load('injectedsignalamp{}.pkl.npy'.format(i),allow_pickle=True)),axis=0)
        injected_signal_optimal_snr = np.concatenate((injected_signal_optimal_snr, np.load('injectedsignaloptimalsnr{}.pkl.npy'.format(i),allow_pickle=True)),axis=0)
        injected_signal_RA = np.concatenate((injected_signal_RA, np.load('injectedsignalRA{}.pkl.npy'.format(i),allow_pickle=True)),axis=0)
        injected_signal_DEC = np.concatenate((injected_signal_DEC, np.load('injectedsignalDEC{}.pkl.npy'.format(i),allow_pickle=True)),axis=0)
        injected_signal_inclination = np.concatenate((injected_signal_inclination, np.load('injectedsignalinclination{}.pkl.npy'.format(i),allow_pickle=True)),axis=0)
    
    
print('done',
len(maximum_noise_snrsignals),
len(injected_signal_freq),
len(injected_signal_tau),
len(injected_signal_amp),
len(injected_signal_optimal_snr),
len(injected_signal_RA),
len(injected_signal_DEC),
len(injected_signal_inclination))

np.save("compliedmaximum_noise_snrsignals.pkl", maximum_noise_snrsignals, allow_pickle=True)
np.save("compliedinjected_signal_freq.pkl", injected_signal_freq, allow_pickle=True)
np.save("compliedinjected_signal_tau.pkl", injected_signal_tau, allow_pickle=True)
np.save("compliedinjected_signal_amp.pkl", injected_signal_amp, allow_pickle=True)
np.save("compliedinjected_signal_optimal_snr.pkl", injected_signal_optimal_snr, allow_pickle=True)
np.save("compliedinjected_signal_RA.pkl", injected_signal_RA, allow_pickle=True)
np.save("compliedinjected_signal_DEC.pkl", injected_signal_DEC, allow_pickle=True)
np.save("compliedinjected_signal_inclination.pkl", injected_signal_inclination, allow_pickle=True)


# condor_rm -all   removes all in queue
#condor_q -analyze <job_id> when held it means error
   