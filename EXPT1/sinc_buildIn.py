import matplotlib.pyplot as plt
import numpy as np

Fs = 10
x = np.linspace(-Fs, Fs, 100)

y = np.sinc(x)

plt.subplot(2,2,1)
plt.plot(x, y)

plt.subplot(2,2,2)
plt.magnitude_spectrum(y)
plt.xlabel('frequency')
plt.ylabel('magnitude')
plt.title('magnitude spectrum')

plt.subplot(2,2,4)
plt.phase_spectrum(y)
plt.title('Phase spectrum')

plt.show()
