
import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display
import glob
from scipy.io import wavfile
import numpy as np
import scipy
from scipy.io.wavfile import read
from scipy.signal import hann
from scipy.fftpack import rfft


counter = 0
total = 0
num_of_female_f = 0
num_of_male_f = 0
no_detection_f = 0
path = "data/all/*.wav"
flag = True
correct_detection = 0
file_name_list = []
for filename in glob.glob(path):
    total += 1
    x, sr = librosa.load(filename)
    X = scipy.fft(x)
    X_mag = numpy.absolute(X)        # spectral magnitude

    if(max(X_mag)>113.32542591236971 or max(X_mag)< 20.865958116020522):
        print('mardddddd')
        flag = False
        if(filename[9] == 'm'):
            correct_detection += 1
            num_of_male_f += 1
    else:
        fs, signal = wavfile.read(filename)
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


        if max(STEs) <12.5 and max(STEs)>5:
            print("male")
            flag = False
            if(filename[9] == 'm'):
                num_of_male_f += 1
                correct_detection += 1
        elif (np.mean(STEs) < 0.7149665232994251 ):
            print("male")
            flag = False
            num_of_male_f += 1
            if(filename[9] == 'm'):
                correct_detection += 1
                num_of_male_f += 1
    if(flag):
        print('female')
        num_of_female_f += 1
        if(filename[9] == 'f'):
            correct_detection += 1
            num_of_female_f += 1

print('accuracy : ', correct_detection/total)
