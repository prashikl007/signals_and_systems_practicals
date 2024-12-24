import numpy as np
import matplotlib.pyplot as plt 


UL = 5
LL = -5
t = np.arange(LL, UL, 0.1)


# Function to generate exponential signals e**(at)
def exponential(a, t): 
    expo =[] 
    for sample in t: 
        expo.append(np.exp( a*sample)) 
    return (expo) 
         

def unit_step(t): 
    unit =[] 
    for sample in t: 
        if sample<0: 
            unit.append(0)
            
        else: 
            unit.append(1) 
    return(unit) 


k = 1
a = 0.35

exp_O = exponential(a, t) 
unit_O = unit_step(t)

y = []
len_t = len(t)
for i in range(len_t):
    x = k * exp_O[i] * unit_O[i]
    y.append(x)


plt.subplot(3,1,1)
plt.plot(t, exp_O)
plt.title('exponential function')
plt.xlabel('time t')
plt.ylabel('magnitude')

plt.subplot(3,1,2)
plt.plot(t, unit_O)
plt.title('Unit Step Function')
plt.xlabel('time t')
plt.ylabel('magnitude')

plt.subplot(3,1,3)
plt.plot(t, y)
plt.title('y = k e –at u(t)')
plt.xlabel('time t')
plt.ylabel('magnitude')

plt.show()
