import numpy as np 
import matplotlib.pyplot as plt 
  
# function to generate unit step u[n-a] 
# LL and UL are lower and upper limits of discrete time line 
def unit_step(a, n): 
    unit =[] 
    for sample in n: 
        if sample<a: 
            unit.append(0)
            
        else: 
            unit.append(1) 
    return(unit) 
  
# plot unit step function u[n-a] 
a = 1 # Enter delay or advance 
UL = 5
LL = -5
n = np.arange(LL, UL, 1) 
unit = unit_step(a, n) 

plt.subplot(2,2,1)
plt.stem(n, unit) 
plt.xlabel('n') 
plt.xticks(np.arange(LL, UL, 1)) 
plt.yticks([0, 1]) 
plt.ylabel('u[n]') 
plt.title('Unit step u[n-a]')

y = np.fft.fft(unit)
plt.subplot(2,2,2)
plt.xlabel('frequency')
plt.ylabel('Magnitude')
plt.plot(y)
plt.title('Magnitude spectrum')

plt.subplot(2,2,3)
plt.phase_spectrum(unit)
plt.title('Phase spectrum')

plt.show()
