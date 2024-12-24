#importing libraries 
import numpy as np
import matplotlib.pyplot as plt 


# Function to generate exponential signals e**(at)

sample=[]
a = -1
UL = 1
LL = -1
n = np.arange(LL, UL, 0.1)
N=-n

def exponential(a, N): 
    expo =[] 
    for sample in n: 
        expo.append(np.exp( a*sample)) 
    return (expo) 
         
x = exponential(a, n) 


plt.subplot(2,2,1)
plt.stem(n, x) 
plt.xlabel('n') 
plt.xticks(np.arange(LL, UL, 0.2)) 
plt.ylabel('x[n]') 
plt.title('Exponential Signal e**(an)')

y = np.fft.fft(x)
plt.subplot(2,2,2)
plt.xlabel('frequency')
plt.ylabel('Magnitude')
plt.plot(y)
plt.title('Magnitude spectrum')

plt.subplot(2,2,3)
plt.phase_spectrum(x)
plt.title('Phase spectrum')


plt.show()
