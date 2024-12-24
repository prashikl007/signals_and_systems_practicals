#importing libraries 
import numpy as np 
import matplotlib.pyplot as plt 
# Function to generate unit ramp signal r(n) 
# r(n)= n for n>= 0, r(n)= 0 otherwise 

def unit_ramp(n): 
    ramp =[] 
    for sample in n: 
        if sample<0: 
            ramp.append(0) 
        else: 
            ramp.append(sample) 
    return ramp 
  
UL = 5
LL = -5
n = np.arange(LL, UL, 0.5) 
r = unit_ramp(n)

plt.subplot(2,2,1)
plt.stem(n, r) 
plt.xlabel('n') 
plt.xticks(np.arange(LL, UL, 1)) 
plt.yticks([0, UL, 1]) 
plt.ylabel('r[n]') 
plt.title('Unit Ramp r[n] in time domain') 

plt.subplot(2,2,2)
plt.xlabel('frequency')
plt.ylabel('Magnitude')
plt.magnitude_spectrum(r)
plt.title('Magnitude spectrum')

plt.subplot(2,2,3)
plt.phase_spectrum(r)
plt.title('Phase spectrum')

plt.show()
