# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 08:51:47 2022

@author: Geraldo Siqueira
"""

import numpy as np
import matplotlib.pyplot as plt

r = 3.6
dt = 0.5
N = 50

def F(x):
    return r*x*(1 - x)

t = np.arange(0,N, dt)
Nt = t.size
x = np.zeros(Nt)

x[0] = (1-1/r) + 0.001
#qx[0] = 0.3

for n in range (1,Nt):
    x[n] = F(x[n-1])
    
plt.title("x vs n (r = 3.57)")
plt.plot(x, 'b.-')