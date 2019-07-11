from __future__ import division
from scipy.io import wavfile
import matplotlib.pyplot as plt
from numpy import linspace
import numpy as np
import math
import statistics 

fName = '../data/female/fsrh0_sx131.wav'

fs, signal = wavfile.read(fName)

DC = statistics.mean(signal)
newSignal = signal - DC                 # create a new signal, preserving old
print ('DC               ==> ', DC)
print ('statistics.mean(newSignal)  ==> ', statistics.mean(newSignal))

assert fs % 1000 == 0

sampsPerMilli = int(fs / 1000)
millisPerFrame = 20
sampsPerFrame = sampsPerMilli * millisPerFrame
nFrames = int(len(signal) / sampsPerFrame)        # number of non-overlapping _full_ frames

print ('samples/millisecond  ==> ', sampsPerMilli)
print ('samples/[%dms]frame  ==> ' % millisPerFrame, sampsPerFrame)
print ('number of frames     ==> ', nFrames)


ZCCs = []                                      # list of short-time zero crossing counts
for i in range(nFrames):
    startIdx = i * sampsPerFrame
    stopIdx = startIdx + sampsPerFrame
    s = newSignal[startIdx:stopIdx]            # /s/ is the frame, named to correspond to the equation
    ZCC = 0
    for k in range(1, len(s)):
        ZCC += 0.5 * abs(np.sign(s[k]) - np.sign(s[k - 1]))
    ZCCs.append(ZCC)

plt.plot(ZCCs)
plt.title('Short-Time Zero Crossing Counts')
plt.ylabel('ZCC')
plt.xlabel('FRAME')
plt.show()