from __future__ import division
from scipy.io import wavfile
import matplotlib.pyplot as plt
from numpy import linspace
import numpy as np
import math
import os
 # pick one file name:
 ###fName = '003_A_male_167Hz.wav'
signal_1_female = []
signal_2_female = []

import glob
female_name_list = glob.glob("/home/zahra/Desktop/6th Semester/Signal/final_project/data/female/*.wav")

for name in female_name_list:
    # fName = '../data/male/mwrp0_sx183.wav'
    fName = name
    fs, signal = wavfile.read(fName)
    signal = signal / max(abs(signal))                        # scale signal
    assert min(signal) >= -1 and max(signal) <= 1
    print ('fs           ==> ', fs, 'Hz')                       # sampling rate
    print ('len(signal)  ==> ', len(signal), 'samples')

    
    # _, (sp1, sp2) = plt.subplots(1, 2, figsize=(16, 4))

    # # plot raw signal
    # sp1.plot(signal)
    # sp1.set_title('Raw Signal')
    # sp1.set_xlabel('SAMPLE\n(a)')
    # sp1.autoscale(tight='both')

    # # plot spectrogram
    # sp2.specgram(signal)
    # sp2.set_title('Spectogram')
    # sp2.set_xlabel('TIME\n(b)')
    # nSecs = len(signal) / fs
    # ticksPerSec = 3
    # nTicks = nSecs * ticksPerSec + 1                # add 1 to include time=0
    # xTickMax = sp2.get_xticks()[-1]
    # sp2.set_xticks(linspace(0, xTickMax, nTicks))
    # sp2.set_xticklabels([round(x, 2) for x in linspace(0, nSecs, nTicks)])
    # sp2.set_ylabel('FREQ')
    # maxFreq = fs / 2
    # nTicks = maxFreq / 1000 + 1                     # add 1 to include freq=0
    # sp2.set_yticks(linspace(0, 1, nTicks))
    # sp2.set_yticklabels(linspace(0, maxFreq, nTicks));
    # sp2.autoscale(tight='both')

    # from IPython import display
    # display.HTML("<audio controls><source src='{}'></audio>".format('../data/female/fsms1_sx64.wav'))

    assert fs % 1000 == 0

    sampsPerMilli = int(fs / 1000)
    millisPerFrame = 20
    sampsPerFrame = sampsPerMilli * millisPerFrame
    nFrames = int(len(signal) / sampsPerFrame)        # number of non-overlapping _full_ frames

    print 'samples/millisecond  ==> ', sampsPerMilli
    print 'samples/[%dms]frame  ==> ' % millisPerFrame, sampsPerFrame
    print 'number of frames     ==> ', nFrames


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
    # plt.xlabel('FRAME')
    # plt.show()
    # pyplot.autoscale(tight='both')
    signal_1_female.append(max(STEs))

    fc = 20
    a = math.exp(-fc * 2 * np.pi / fs)
    STEs = []
    for n in range(len(signal)):
        if n == 0:
            STEs.append(a * 0 + signal[n] ** 2)           # base-case
        else:
            STEs.append(a * STEs[n - 1] + signal[n] ** 2)

    signal_2_female.append(max(STEs))
    # plt.plot(STEs)
    # plt.title('Short-Time Energy')
    # plt.ylabel('ENERGY')
    # plt.xlabel('SAMPLE')
    # plt.show()
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

sum1= sum(signal_1_female)
sum2 = sum(signal_2_female)
avg1 = sum1/len(signal_1_female)
avg2 = sum2/len(signal_2_female)

with open ("result1_f.txt", "w") as file1:
    file1.write(str(signal_1_female)+"\nAverage:%s"%avg1)

with open ("result2_f.txt", "w") as file1:
    file1.write(str(signal_2_female)+"\nAverage:%s"%avg2)
print(max(signal_1_female))
print(min(signal_1_female))
print(max(signal_2_female))
print(min(signal_2_female))


import glob
male_name_list = glob.glob("/home/zahra/Desktop/6th Semester/Signal/final_project/data/male/*.wav")
signal_1_male = []
signal_2_male = []
for name in male_name_list:
    # fName = '../data/male/mwrp0_sx183.wav'
    fName = name
    fs, signal = wavfile.read(fName)
    signal = signal / max(abs(signal))                        # scale signal
    assert min(signal) >= -1 and max(signal) <= 1
    print ('fs           ==> ', fs, 'Hz')                       # sampling rate
    print ('len(signal)  ==> ', len(signal), 'samples')


    assert fs % 1000 == 0

    sampsPerMilli = int(fs / 1000)
    millisPerFrame = 20
    sampsPerFrame = sampsPerMilli * millisPerFrame
    nFrames = int(len(signal) / sampsPerFrame)        # number of non-overlapping _full_ frames

    print 'samples/millisecond  ==> ', sampsPerMilli
    print 'samples/[%dms]frame  ==> ' % millisPerFrame, sampsPerFrame
    print 'number of frames     ==> ', nFrames


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
    # plt.xlabel('FRAME')
    # plt.show()
    # pyplot.autoscale(tight='both')
    signal_1_male.append(max(STEs))

    fc = 20
    a = math.exp(-fc * 2 * np.pi / fs)
    STEs = []
    for n in range(len(signal)):
        if n == 0:
            STEs.append(a * 0 + signal[n] ** 2)           # base-case
        else:
            STEs.append(a * STEs[n - 1] + signal[n] ** 2)

    signal_2_male.append(max(STEs))
    # plt.plot(STEs)
    # plt.title('Short-Time Energy')
    # plt.ylabel('ENERGY')
    # plt.xlabel('SAMPLE')
    # plt.show()
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

sum1= sum(signal_1_male)
sum2 = sum(signal_2_male)
avg1 = sum1/len(signal_1_male)
avg2 = sum2/len(signal_2_male)

with open ("result1_m.txt", "w") as file1:
    file1.write(str(signal_1_male)+"\nAverage:%s"%avg1)

with open ("result2_m.txt", "w") as file1:
    file1.write(str(signal_2_male)+"\nAverage:%s"%avg2)
print(max(signal_1_male))
print(min(signal_1_male))
print(max(signal_2_male))
print(min(signal_2_male))