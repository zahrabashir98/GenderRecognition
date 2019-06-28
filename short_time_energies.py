from __future__ import division
from scipy.io import wavfile
import matplotlib.pyplot as plt
from numpy import linspace
import numpy as np

 # pick one file name:
 ###fName = '003_A_male_167Hz.wav'
fName = '../data/female/fsms1_sx64.wav'

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

from IPython import display
display.HTML("<audio controls><source src='{}'></audio>".format('../data/female/fsms1_sx64.wav'))

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

plt.plot(STEs)
plt.title('Short-Time Energy')
plt.ylabel('ENERGY')
plt.xlabel('FRAME')
plt.show()
# pyplot.autoscale(tight='both')
