import numpy as np
import pyaudio
import wave
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display
import glob
from scipy.io import wavfile
import numpy as np


def recognize(filename):

    flag = True
    x, sr = librosa.load(filename)
    X = scipy.fft(x)
    X_mag = numpy.absolute(X)        # spectral magnitude

    if(max(X_mag)>113.32542591236971 or max(X_mag)< 20.865958116020522):
        print('mardddddd')
        flag = False

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

    if(flag):
        print('female')


"Default values"
RATE = 20000
RECORD_SECONDS = 2

FORMAT = pyaudio.paInt16
CHANNELS = 1
CHUNK = 1024

WAVE_OUTPUT_FILENAME = "output.wav"
audio = pyaudio.PyAudio()
flag = True
while (True):
    print("start recording")
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    # rate, data = wav.read(WAVE_OUTPUT_FILENAME)
    recognize(WAVE_OUTPUT_FILENAME)    
    print("end of record\n")


