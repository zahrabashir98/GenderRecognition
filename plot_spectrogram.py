"""
======================================
Spectrogram, power spectral density
======================================

Demo spectrogram and power spectral density on a frequency chirp.
"""

import numpy as np
from matplotlib import pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft
from scipy.io import wavfile as wav
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import math

samplerate, data = wav.read('../data/female/fsms1_sx64.wav')
############################################################
# Generate a chirp signal
############################################################

# Seed the random number generator
np.random.seed(0)

# A signal with a small frequency chirp
# sig = np.sin(0.5 * np.pi * time_vec * (1 + .1 * time_vec))
sig = data
plt.figure(figsize=(8, 5))

time_step = .01
time_vec = np.arange(0, len(sig))

plt.plot(time_vec, sig)

############################################################
# Compute and plot the spectrogram
############################################################
#
# The spectrum of the signal on consecutive time windows

from scipy import signal
freqs, times, spectrogram = signal.spectrogram(sig)

plt.figure(figsize=(5, 4))
plt.imshow(spectrogram, aspect='auto', cmap='hot_r', origin='lower')
plt.title('Spectrogram')
plt.ylabel('Frequency band')
plt.xlabel('Time window')
plt.tight_layout()


############################################################
# Compute and plot the power spectral density (PSD)
############################################################
#
# The power of the signal per frequency band

freqs, psd = signal.welch(sig)

plt.figure(figsize=(5, 4))
plt.semilogx(freqs, psd)
plt.title('PSD: power spectral density')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.tight_layout()

############################################################

plt.show()


