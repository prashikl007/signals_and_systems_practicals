#importing libraries 
import numpy as np
import matplotlib.pyplot as plt
#from scipy.fftpack import fft

Fs = samples = 10000
n = np.arange(samples)
t = n/samples

f1 = 200
f2 = 200

x = np.sin(2*np.pi*f1*t)
x1 = 0.5*np.sin(2*np.pi*f2*t + np.pi/6)
y = x 

#Y = fft(y)

#Y_m = (2/Fs)*abs(Y)

#Y_phase = (2/Fs)*np.angle(Y)

plt.subplot(2,1,1)
plt.plot(t, x)
plt.title('sin(2*np.pi*f*t)')
plt.xlabel('time t')
plt.ylabel('magnitude')

plt.subplot(2,1,2)
plt.plot(t, x1)
plt.title('sin(2*np.pi*f*t+ np.pi/6)')
plt.xlabel('time t')
plt.ylabel('magnitude')

'''plt.subplot(2,2,3)
plt.plot(Y_m)
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency Hz')
plt.ylabel('Magnitude')

plt.subplot(2,2,4)
plt.plot(Y_phase)
plt.title('Phase Spectrum')
plt.xlabel('n')
plt.ylabel('Phase in radians')

plt.subplot(2,2,2)
plt.magnitude_spectrum(y)

plt.subplot(2,2,3)
plt.phase_spectrum(y)'''

plt.show()
