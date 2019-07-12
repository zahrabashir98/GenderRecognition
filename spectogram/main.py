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
allpsd_list_f = []
correct_f = 0
incorrect_f = 0
correct_m = 0
incorrect_m = 0

for name in female_name_list:

    samplerate, data = wav.read(name)
    sig = data
    freqs, times, spectrogram = signal.spectrogram(sig)

    freqs, psd = signal.welch(sig)
    psdList_female.append(max(psd))
    allpsd_list_f.append(psd)
    average = sum(psd)/len(psd)
    if average <96000:
        print("male")
        incorrect_f += 1
    elif average> 96000 and average <441970:
        print("Female")
        correct_f += 1
    elif average >441970 and average <2000000:
        print("male")
        incorrect_f += 1

    elif average > 2000000:
        print("male")
        incorrect_f += 1
    # if max(psd) > 60261851:
    #     print("female")
    #     female_correct += 1
    # elif max(psd) < 512442:
    #     female_wrong += 1
    #     print("male")
    # else:
    #     # print("nooo")
    #     female_no_det += 1
# print(psdList_female)


male_correct = 0
male_wrong = 0
male_no_det = 0
allpsd_list_m = []

male_name_list = glob.glob("/home/zahra/Desktop/6th Semester/Signal/final_project/data/male/*.wav")
psdList_male = []
for name in male_name_list:

    samplerate, data = wav.read(name)
    sig = data
    freqs, times, spectrogram = signal.spectrogram(sig)

    freqs, psd = signal.welch(sig)
    psdList_male.append(max(psd))
    allpsd_list_m.append(psd)

    average = sum(psd)/len(psd)
    if average <96000:
        print("male")
        correct_m += 1
    elif average> 96000 and average <441970:
        print("Female")
        incorrect_m += 1
    
    elif average >441970 and average <2000000:
        print("male")
        correct_m += 1

    elif average > 2000000:
        print("male")
        correct_m += 1

    # if max(psd) > 60261851:
    #     print("female")
    #     male_correct += 1
    # elif max(psd) < 512442:
    #     male_wrong += 1
    #     print("male")
    # else:
    #     # print("noo")
    #     male_no_det += 1
# print(psdList_male)
# print(max(psdList_female))
# print(min(psdList_female))
# print(max(psdList_male))
# print(min(psdList_male))
print("Female_ACC: ", correct_f/len(female_name_list))
print("Male_ACC: ", correct_m/len(male_name_list))

summ = 0
av_1 = []
for data in allpsd_list_f:
    summ = sum(data)
    average = summ/len(data)
    av_1.append(average)
av_1.sort()
# print(av_1)
# print(sum(av_1)/len(av_1))


summ = 0
av_2 = []
for data in allpsd_list_m:
    summ = sum(data)
    average = summ/len(data)
    av_2.append(average)
av_2.sort()
# print(av_2)
# print(sum(av_2)/ len(av_2))

with open("results.txt", "w") as file1:
    file1.write("FEMALE:\naverage_psd: %s\nmax_psd:%s\nmin_psd:%s\n\nMALE:\naverage_psd: %s\nmax_psd:%s\nmin_psd:%s\n\n"
    %(sum(av_1)/ len(av_1),max(psdList_female),min(psdList_female),sum(av_2)/ len(av_2), max(psdList_male), min(psdList_male)))

