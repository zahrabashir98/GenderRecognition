import numpy as np
from scipy.fftpack import fft, ifft
from scipy.io import wavfile as wav
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import math

samplerate, data = wav.read('../data/female/fsms1_sx64.wav')
# signalFFT = fft(data)
# plt.plot(signalFFT)
# plt.show()

samplerate, dataM = wav.read('../data/male/mwad0_sx72.wav')
# signalFFT = fft(dataM)
# plt.plot(signalFFT)
# plt.show()

a = np.zeros(len(data))

for x in data:
    
# RMS
# l = []
# for x in data:
#     l.append(math.sqrt(np.mean(x*x)))
# plt.plot(np.array(l))
# plt.show()


#######################################################
# n = len(data) 
# p = fft(data) # take the fourier transform 
# nUniquePts = int(math.ceil((n+1)/2.0))
# p = p[0:nUniquePts]
# p = abs(p)

# p = p / float(n) # scale by the number of points so that
#                  # the magnitude does not depend on the length 
#                  # of the signal or on its sampling frequency  
# p = p**2  # square it to get the power 

# # multiply by two (see technical document for details)
# # odd nfft excludes Nyquist point
# if n % 2 > 0: # we've got odd number of points fft
#     p[1:len(p)] = p[1:len(p)] * 2
# else:
#     p[1:len(p) -1] = p[1:len(p) - 1] * 2 # we've got even number of points fft

# freqArray = np.arange(0, nUniquePts, 1.0) * (samplerate / n);
# plt.plot(freqArray/1000, 10*math.log10(p), color='k')
# xlabel('Frequency (kHz)')
# ylabel('Power (dB)')
# plt.show()
# rms_val = sqrt(mean(data**2))
# print(rms_val)
