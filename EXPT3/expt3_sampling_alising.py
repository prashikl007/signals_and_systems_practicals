# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 12:46:21 2021

@author: PRASHIK
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

Fs = samples = 1000
n = np.arange(samples)
t = n/samples

fc = 300
fc1 = fc + 100
fc2 = fc - 100

xc = np.sin(2*np.pi*fc*t)
xfc1 = 0.5*np.sin(2*np.pi*fc1*t)
xfc2 = 0.5*np.sin(2*np.pi*fc2*t)

y = xc + xfc1 + xfc2 

Y = fft(y)    #taking FFT
Y_m = (2/Fs)*abs(Y)     #magnitude spectrum
Y_phase = (2/Fs)*np.angle(Y)     #phase spectrum

plt.subplot(3,2,1)
plt.plot(t, xc)
plt.title('X fc')
plt.xlabel('time t')
plt.ylabel('magnitude')

plt.subplot(3,2,2)
plt.plot(t, xfc1)
plt.title('X fc1')
plt.xlabel('time t')
plt.ylabel('magnitude')

plt.subplot(3,2,3)
plt.plot(t, xfc2)
plt.title('X fc2')
plt.xlabel('time t')
plt.ylabel('magnitude')

plt.subplot(3,2,4)
plt.plot(t, y)
plt.title('y = xfc + xfc1 + xfc2')
plt.xlabel('time t')
plt.ylabel('magnitude')

plt.subplot(3,2,5)
plt.plot(Y_m)
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency Hz')
plt.ylabel('Magnitude')

'''
plt.subplot(3,2,5)
plt.magnitude_spectrum(y, Fs)

plt.subplot(3,2,6)
plt.plot(Y_phase)
plt.title('Phase Spectrum')
plt.xlabel('n')
plt.ylabel('Phase in radians')
'''

plt.subplot(3,2,6)
plt.phase_spectrum(y)

plt.show()
