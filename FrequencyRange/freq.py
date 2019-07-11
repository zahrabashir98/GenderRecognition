from scipy.io import wavfile
import matplotlib.pyplot as plt
from numpy import linspace
import numpy as np
import math
import os
import glob
# import fft
from scipy.fftpack import fft, ifft

# female_name_list = glob.glob("/home/zahra/Desktop/6th Semester/Signal/final_project/data/female/*.wav")

fName = '../../data/female/ftlg0_sx123.wav'
fs, signal = wavfile.read(fName)
signalFFT1 = fft(signal)
x1 = np.arange(0, fs)
chart1 = plt.subplot(221)
plt.title('1')
plt.plot(x1, signalFFT1[0:fs])

# fName = '../../data/male/mwjg0_sx224.wav'
fName = '../../data/female/ftmg0_sx272.wav'
fs, signal = wavfile.read(fName)
signalFFT1 = fft(signal)
x1 = np.arange(0, fs)
chart1 = plt.subplot(222)
plt.title('2')
plt.plot(x1, signalFFT1[0:fs])

# fName = '../../data/male/mwrp0_sx183.wav'
fName = '../../data/female/fvkb0_sx439.wav'
fs, signal = wavfile.read(fName)
signalFFT1 = fft(signal)
x1 = np.arange(0, fs)
chart1 = plt.subplot(223)
plt.title('3')
plt.plot(x1, signalFFT1[0:fs])

# fName = '../../data/male/mwsh0_sx436.wav'
fName = '../../data/female/fvfb0_sx222.wav'
fs, signal = wavfile.read(fName)
signalFFT1 = fft(signal)
x1 = np.arange(0, fs)
chart1 = plt.subplot(224)
plt.title('4')
plt.plot(x1, signalFFT1[0:fs])

plt.show()