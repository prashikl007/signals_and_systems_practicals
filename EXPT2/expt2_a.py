import numpy as np
import matplotlib.pyplot as plt

Fs = samples = 10000
n = np.arange(samples)
t = n/samples

f = 100

x = np.cos(2*np.pi*f*t)

x1 = np.cos(2*np.pi*f*t + np.pi/6)

plt.subplot(2,1,1)
plt.plot(t, x)
plt.title('sin(2*np.pi*f*t)')
plt.xlabel('time t')
plt.ylabel('magnitude')

plt.subplot(2,1,2)
plt.plot(t, x1)
plt.title('sin(2*np.pi*f*t + np.pi/6)')
plt.xlabel('time t')
plt.ylabel('magnitude')

plt.show()
