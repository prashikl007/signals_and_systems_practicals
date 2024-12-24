import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

Fs = 1000
n = np.arange(Fs)
t = n/Fs

fc = 300

xc = np.sin(2*np.pi*fc*t)


Y = fft(xc)    #taking FFT
Y_m = (2/Fs)*abs(Y)     #magnitude spectrum

plt.subplot(3,2,1)
plt.plot(t, xc)
plt.title('X fc')
plt.xlabel('time t')
plt.ylabel('magnitude')


plt.subplot(3,2,2)
plt.plot(Y_m)
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency Hz')
plt.ylabel('Magnitude')

plt.show()
