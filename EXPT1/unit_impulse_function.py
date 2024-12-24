import numpy as np 
import matplotlib.pyplot as plt 

# Function to plot Impulse signal d(a) 
def unit_impulse(a, n): 
    delta = [] 
    for sample in n: 
        if sample == a: 
            delta.append(1) 
        else: 
            delta.append(0) 
              
    return delta 
  
a = 2 # Enter delay or advance 
UL = 10
LL = -10
n = np.arange(LL, UL, 1) 
d = unit_impulse(a, n) 

#calculating amplitude spectrum usinf fft
y = np.fft.fft(d)

Y_mag = abs(y)   #this gives magnitude of spectrum

plt.subplot(2,2,1)
plt.stem(n, d) 
plt.xlabel('n') 
plt.xticks(np.arange(LL, UL, 1)) 
plt.yticks([0, 1]) 
plt.ylabel('d[n]') 

plt.subplot(2,2,2)
plt.xlabel('frequency')
plt.ylabel('Magnitude')
plt.plot(Y_mag)

plt.subplot(2,2,3)
plt.phase_spectrum(d) # this shows phase of signal

plt.show()
