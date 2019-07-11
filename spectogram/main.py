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
import glob
from scipy import signal

female_name_list = glob.glob("/home/zahra/Desktop/6th Semester/Signal/final_project/data/female/*.wav")
psdList_female = []
female_correct = 0
female_wrong = 0
female_no_det = 0
for name in female_name_list:

    samplerate, data = wav.read(name)
    sig = data
    freqs, times, spectrogram = signal.spectrogram(sig)

    freqs, psd = signal.welch(sig)
    psdList_female.append(max(psd))

    if max(psd) > 60261851:
        print("female")
        female_correct += 1
    elif max(psd) < 512442:
        female_wrong += 1
        print("male")
    else:
        print("nooo")
        female_no_det += 1

# print(psdList_female)
# print(max(psdList_female))
# print(min(psdList_female))

male_correct = 0
male_wrong = 0
male_no_det = 0

male_name_list = glob.glob("/home/zahra/Desktop/6th Semester/Signal/final_project/data/male/*.wav")
psdList_male = []
for name in male_name_list:

    samplerate, data = wav.read(name)
    sig = data
    freqs, times, spectrogram = signal.spectrogram(sig)

    freqs, psd = signal.welch(sig)
    psdList_male.append(max(psd))
    
    if max(psd) > 60261851:
        print("female")
        male_correct += 1
    elif max(psd) < 512442:
        male_wrong += 1
        print("male")
    else:
        print("noo")
        male_no_det += 1

# print(psdList_male)
# print(max(psdList_male))
# print(min(psdList_male))
