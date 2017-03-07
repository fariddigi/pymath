# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np
def f(x):
    pi= np.pi;
    e= np.e;
    j= complex(0,1);
    return e**(j*pi*x)
 
x= np.arange(0,np.pi,0.1)
j= complex(0,1);
print(f(x))
plt.figure(1)
plt.grid(True);
#plt.plot(x,f(x))
plt.polar(x, abs(f(x)),'ro-' )
plt.show()
plt.figure(2)
plt.grid(True);
#plt.plot(x,f(x))
plt.plot(x, np.angle(f(x)),'ro-' )
plt.show()