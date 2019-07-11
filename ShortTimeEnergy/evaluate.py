from __future__ import division
from scipy.io import wavfile
import matplotlib.pyplot as plt
from numpy import linspace
import numpy as np
import math
import os
import glob

# fName = '../../data/male/mwrp0_sx183.wav'
female_name_list = glob.glob("/home/zahra/Desktop/6th Semester/Signal/final_project/data/female/*.wav")
num_of_female_f = 0
num_of_male_f = 0
no_detection_f = 0



for name in female_name_list:
    fs, signal = wavfile.read(name)
    signal = signal / max(abs(signal))                        # scale signal
    assert min(signal) >= -1 and max(signal) <= 1
    assert fs % 1000 == 0

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

    # plt.plot(STEs)
    # plt.title('Short-Time Energy')
    # plt.ylabel('ENERGY')
    # plt.xlabel('SAMPLE')
    # plt.show()

    if max(STEs) <12.5 and max(STEs)>5:
        print("male")
        num_of_male_f += 1
    elif max(STEs) >29:
        print("female")
        num_of_female_f += 1
    else:
        if max(STEs) <20:
            num_of_male_f += 1
        elif max>20:
            num_of_female_f += 1
        # print("BISEXUAL ")
        # no_detection_f += 0
print(num_of_female_f)
print(num_of_male_f)
acc_f = num_of_female_f/len(female_name_list)
print("ACCURACY:",acc_f)
##############################################################

num_of_female_m = 0
num_of_male_m = 0
no_detection_m = 0
male_name_list = glob.glob("/home/zahra/Desktop/6th Semester/Signal/final_project/data/male/*.wav")
for name in male_name_list:
    fs, signal = wavfile.read(name)
    signal = signal / max(abs(signal))                        # scale signal
    assert min(signal) >= -1 and max(signal) <= 1

    assert fs % 1000 == 0

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

    # plt.plot(STEs)
    # plt.title('Short-Time Energy')
    # plt.ylabel('ENERGY')
    # plt.xlabel('SAMPLE')
    # plt.show()

    if max(STEs) <12.5 and max(STEs)>5:
        print("male")
        num_of_male_m += 1
    elif max(STEs) >29:
        print("female")
        num_of_female_m += 1
    else:
        if max(STEs) <20:
            num_of_male_m += 1
        elif max>20:
            num_of_female_m += 1
        # print("BISEXUAL ")
        # no_detection_m += 0
    
print(num_of_female_m)
print(num_of_male_m)
acc_m = num_of_male_m/len(male_name_list)
print("ACCURACY:",acc_m)

with open("final_results.txt","w") as File:
    File.write("FEMALE:\nnum_of_female_f:%s\nnum_of_male_f:%s\nacc:%s\n*******\nMALE:\nnum_of_female_f:%s\nnum_of_male_f:%s\nacc:%s\n*******"%(num_of_female_f, num_of_male_f, acc_f, num_of_female_m, num_of_male_m, acc_m))