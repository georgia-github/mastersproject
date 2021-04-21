#!/usr/bin/env python
"""
A script to show how to create your own time domain source model.
A simple damped Gaussian signal is defined in the time domain, injected into
noise in two interferometers (LIGO Livingston and Hanford at design
sensitivity), and then recovered.
"""

import numpy as np
import bilby


# define the time-domain model
def time_domain_damped_sinusoid(
        time, amplitude, damping_time, frequency, phase, t0):
    """
    This example only creates a linearly polarised signal with only plus
    polarisation.
    """
    plus = np.zeros(len(time))
    tidx = time >= t0
    plus[tidx] = amplitude * np.exp(-(time[tidx] - t0) / damping_time) *\
        np.sin(2 * np.pi * frequency * (time[tidx] - t0) + phase)
    cross = np.zeros(len(time))
    return {'plus': plus, 'cross': cross}


# define parameters to inject.
injection_parameters = dict(amplitude=5e-22, damping_time=0.1, frequency=1383.6704685625616,
                            phase=0, ra=0, dec=0, psi=0, t0=0., geocent_time=0.)

duration = 2
sampling_frequency = 16384

outdir = 'outdir6'
label = 'PSR_B0833-45'
run = 'test'


detector = 'H1'
channel_name = "H1:DCS-CALIB_STRAIN_C02"



# call the waveform_generator to create our waveform model.
waveform = bilby.gw.waveform_generator.WaveformGenerator(
    duration=duration, sampling_frequency=sampling_frequency,
    time_domain_source_model=time_domain_damped_sinusoid,
    start_time=injection_parameters['geocent_time'] - 0.5)


detectors = ['H1']
channel_names = ["H1:DCS-CALIB_STRAIN_C02"]


duration = 2
psd_duration = 128
minimum_frequency = 1200# Hz
sampling_frequency = 16384
sample_rate = 16384
eventtime = 1165577780 #max glitch snr time
gpsstart = eventtime - (duration/2)
gpsend = eventtime + (duration/2)
psd_start_time = gpsstart + duration
psd_end_time = psd_start_time + psd_duration






# Set up interferometer objects from the cache files
interferometers = bilby.gw.detector.InterferometerList([])

for channel_name in channel_names:
    interferometer = bilby.gw.detector.load_data_by_channel_name(
        start_time=gpsstart, segment_duration=duration,
        psd_duration=psd_duration, psd_start_time=psd_start_time,
        channel_name=channel_name, sampling_frequency=sampling_frequency, outdir=outdir)
    interferometer.minimum_frequency = minimum_frequency
    interferometers.append(interferometer)

ifos = interferometers



#  create the priors
prior = injection_parameters.copy()
prior['amplitude'] = bilby.core.prior.LogUniform(1e-23, 1e-21, r'$h_0$')
prior['damping_time'] = bilby.core.prior.Uniform(0.05, 0.5, r'damping time', unit='$s$')
prior['frequency'] = bilby.core.prior.Uniform(1283.6704685625616, 1483.6704685625616, r'frequency', unit='Hz') # these need to be close to signal
prior['phase'] = bilby.core.prior.Uniform(-np.pi / 2, np.pi / 2, r'$\phi$')
prior['ra'] = 2.24861032181722
prior['dec'] = -0.78847612466068
prior['psi'] = bilby.core.prior.Uniform(0, np.pi / 2, r'psi')
prior['t0'] = bilby.core.prior.Uniform(gpsstart-1,gpsstart+1)

# define likelihood
likelihood = bilby.gw.likelihood.GravitationalWaveTransient(ifos, waveform)

# launch sampler
result = bilby.core.sampler.run_sampler(
    likelihood, prior, sampler='dynesty', npoints=1000,
    injection_parameters=injection_parameters, outdir=outdir, label=label)

result.plot_corner()
