import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import  glob

def get_pitch(fs,x):
    ms20=int((fs/50))
    ms2=int(fs/500)

    x=[i/32767 for i in x]

    y=plt.acorr(x,maxlags=ms20,normed=True)

    y=y[1]
    z=y[round(len(y)/2):]
    z=z[ms2:ms20]
    zmax=max(z)

    index=np.where(z==zmax)
    index=index[0][0]

    pitch=fs/(ms2+index+2)

    return pitch


female_name_list = glob.glob("/home/zahra/Desktop/6th Semester/Signal/final_project/data/female/*.wav")
female_list = []

for name in female_name_list:   
    fs, signal = wavfile.read(name)
    female_list.append(get_pitch(fs,signal))


male_name_list = glob.glob("/home/zahra/Desktop/6th Semester/Signal/final_project/data/male/*.wav")
male_list = []

for name in male_name_list:   
    fs, signal = wavfile.read(name)
    male_list.append(get_pitch(fs,signal))

print(max(female_list))
print(min(female_list))
print()
print(max(male_list))
print(min(male_list))