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
avg_list_f = []

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
    count = 0
    summ = 0
    for data in STEs:
        if data >0.01:
            summ += data
            count += 1
    print(summ/count)
    avg_list_f.append(summ/count)
    print(sum(STEs)/len(STEs))

    # # print(STEs)
    # print(sum(STEs)/len(STEs))
    # print(max(STEs))
    # print(min(STEs))
    print("**********************")
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
        elif max(STEs)>20:
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
avg_list_m = []
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
    summ = 0
    count = 0
    for data in STEs:
        if data >0.01:
            summ += data
            count += 1
    print(summ/count)
    print(sum(STEs)/len(STEs))
    avg_list_m.append(summ/count)
    # print(max(STEs))
    # print(min(STEs))
    print("**********************")
    if max(STEs) <12.5 and max(STEs)>5:
        print("male")
        num_of_male_m += 1
    elif max(STEs) >29:
        print("female")
        num_of_female_m += 1
    else:
        if max(STEs) < 20:
            num_of_male_m += 1
        elif max(STEs) > 20:
            num_of_female_m += 1
        # print("BISEXUAL ")
        # no_detection_m += 0
    
print(num_of_female_m)
print(num_of_male_m)
acc_m = num_of_male_m/len(male_name_list)
print("ACCURACY:",acc_m)

with open("final_results.txt","w") as File:
    File.write("FEMALE:\nnum_of_female_f:%s\nnum_of_male_f:%s\nacc:%s\n*******\nMALE:\nnum_of_female_f:%s\nnum_of_male_f:%s\nacc:%s\n*******"%(num_of_female_f, num_of_male_f, acc_f, num_of_female_m, num_of_male_m, acc_m))

avg_list_f.sort()
avg_list_m.sort()   
print(avg_list_f)
print("AVG",sum(avg_list_f)/len(avg_list_f))
print("median",avg_list_f[int(len(avg_list_f)/2)])
print("******************************")
print(avg_list_m)
print("AVG", sum(avg_list_m)/len(avg_list_m))
print("median", avg_list_m[int(len(avg_list_m)/2)])



# some imporved rules:
# if avg_energy > 2:
#     print("female")
# elif avg_energy <1.06 :
#     #ghatiii
#     print("male")
# elif avg_energy >1.06 and avg_energy <2:
#     print("no idea")
