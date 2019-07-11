
import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display
import glob


counter = 0
koll = 0
path = "../data/female/*.wav"
a = []
for filename in glob.glob(path):
    koll += 1
    
    x, sr = librosa.load(filename)

    X = scipy.fft(x)
    X_mag = numpy.absolute(X)        # spectral magnitude
    # f = numpy.linspace(0, sr, len(x))  # frequency variable
    if(max(X_mag)>113.32542591236971 or max(X_mag)< 20.865958116020522):
        print('mard')
        counter += 1
    else:
        print('zzzzzzan')
    # plt.figure(figsize=(14, 5))
    # plt.plot(f[:2000], X_mag[:2000]) # magnitude spectrum
    # plt.xlabel('Frequency (Hz)')
    # plt.show()

print(counter)
print(koll)
# print(a)
# print(max(a))
# print(min(a))