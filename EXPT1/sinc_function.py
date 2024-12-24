import matplotlib.pyplot as plt
import numpy as np
import math



Fs = 10000   # define sampling frequence
n = np.arange(-Fs, Fs, 1)  
t=n/Fs

i = 0
x = []
f = 100   # define frequency of signal
y1 = []
y2 = []
y = []

while i < 2*Fs :
    x.append(2*f*t[i])
    y1.append(np.sin(x[i]*np.pi))
    y2.append(x[i]*np.pi)
    y.append(y1[i]/y2[i])
    if (math.isnan(y[i])):
        y[i]=0
    #print('i=', i, 't=', t[i], 'x=', x[i], 'y1=', y1[i], 'y2=', y2[i], 'y=', y[i])
    i=i+1

plt.subplot(2,2,1)
plt.plot(x,y)
plt.title('sinc(x)')
plt.xlabel('x')
plt.ylabel('sinc(x)')

plt.subplot(2,2,2)
plt.magnitude_spectrum(y)

plt.subplot(2,2,3)
plt.phase_spectrum(y)

plt.show()
