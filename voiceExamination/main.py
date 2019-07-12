import numpy as np
import wave
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display
import glob
from scipy.io import wavfile
import numpy as np

rate, tmp = wav.read("2.wav")
print(tmp)
data = []
for i in tmp:
    data.append(i[0])
data = np.array(data)
print(data)
