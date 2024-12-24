# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 16:08:26 2021

@author: PRASHIK
"""

import numpy as np 
import matplotlib.pyplot as plt 

# LL and UL are lower and upper limits of discrete time line 
def rect_angular(a, T): 
    mag =[]
    UL = T + 5
    LL = (-T) - 5  
    n = np.arange(LL, UL, 1)
    for sample in n: 
        if (sample >= (-T)) and (sample <= T): 
            mag.append(a)
            
        else: 
            mag.append(0) 
    return(mag, n) 

a = 1 # Amplitude 
T = 5 # Time period

 
rect, n = rect_angular(a, T) 

plt.subplot(2,2,1)
plt.plot(n, rect)
#plt.stem(n, rect) 
plt.xlabel('n') 
#plt.xticks(np.arange(T+5, T-5, 1)) 
#plt.yticks([0, 1]) 
plt.ylabel('u[n]') 
plt.title('')

y = np.fft.fft(rect)
plt.subplot(2,2,2)
plt.xlabel('frequency')
plt.ylabel('Magnitude')
plt.plot(y)
plt.title('Magnitude spectrum')

plt.subplot(2,2,3)
plt.phase_spectrum(rect)
plt.title('Phase spectrum')

plt.show()
