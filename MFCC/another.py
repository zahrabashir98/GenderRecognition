import librosa
import numpy as np
import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display
import glob
from scipy.io import wavfile
import numpy as np

def get_mfcc(y,sr):
    y = librosa.resample(y, sr, 8000)
    y = y[0:40000]
    y = np.concatenate((y, [0]* (40000 - y.shape[0])), axis=0)
      #Mel-frequency cepstral coefficients 
    mfcc=librosa.feature.mfcc(y=y, sr=sr, n_mfcc=10,hop_length=4000)
    mfcc_feature=np.reshape(mfcc, (1,110))
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(mfcc_feature, x_axis='time')
    plt.colorbar()
    plt.title('MFCC')
    plt.tight_layout()
    plt.show()

    return mfcc_feature

y, sr = librosa.load('../../data/female/ftlg0_sx33.wav')
print(get_mfcc(y,sr))