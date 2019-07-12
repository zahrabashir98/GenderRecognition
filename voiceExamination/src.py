
import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display
import glob
from scipy.io import wavfile as wav
import numpy as np
import scipy
from scipy.io.wavfile import read
from scipy.signal import hann
from scipy.fftpack import rfft
from scipy import signal


rate, tmp = wav.read("new.wav")
signal = tmp
# print(tmp)
# data = []
# for i in tmp:
#     data.append(i[0])
# data = np.array(data)

# print(data)
# signal = data
# average = 0
fs = rate
# print(rate)
# freqs, times, spectrogram = signal.spectrogram(sig)
# freqs, psd = signal.welch(sig)
# average = sum(psd)/len(psd)
# print(average)

# if average <96000:
#     print("male")

# elif average> 96000 and average <441970:
#     print("Female")
# elif average >441970 and average <2000000:
#     print("male")


# elif average > 2000000:
#     print("male")
# fs, signal = wavfile.read(filename)
signal = signal / max(abs(signal))                        # scale signal
assert min(signal) >= -1 and max(signal) <= 1
# assert fs % 1000 == 0

sampsPerMilli = int(fs / 1000)
millisPerFrame = 20
sampsPerFrame = sampsPerMilli * millisPerFrame
nFrames = int(len(signal) / sampsPerFrame)        # number of non-overlapping _full_ frames

STEs = []                                      # list of short-time energies
for k in range(nFrames):
    startIdx = k * sampsPerFrame
    stopIdx = startIdx + sampsPerFrame
    window = np.zeros(signal.shape)
    window[startIdx:stopIdx] = 1               # rectangular window
    STE = sum((signal ** 2) * (window ** 2))
    STEs.append(STE)

if max(STEs) <12.5 and max(STEs)>5:
        print("male")
elif max(STEs) >29:
    print("female")

else:
    if max(STEs) < 20:
        print("male")
    elif max(STEs) > 20:
        print("Female")
    
