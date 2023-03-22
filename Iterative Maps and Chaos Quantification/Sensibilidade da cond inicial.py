# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 13:24:12 2022

@author: Geraldo Siqueira
"""

import numpy as np
import matplotlib.pyplot as plt

r = 3.73
dt = 0.5
N = 200

def F(x):
    return r*x*(1 - x)

t = np.arange(0,N, dt)
Nt = t.size
x1 = np.zeros(Nt)
x2 = np.zeros(Nt)

x1[0] = 0.1
x2[0] = 0.1

for n in range (1,Nt):
    x1[n] = F(x1[n-1])
    
    
for n in range (1,Nt):
    x2[n-1] = x2[n-1]/10
    x2[n-1] = x2[n-1]*10
    x2[n] = F(x2[n-1])
    
    
plt.title("x vs n (r = 3.73)")
plt.plot(x1, 'b.-')
plt.plot(x2, 'r.-')
plt.xlim(100, 200)