# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 10:21:43 2022

@author: Geraldo Siqueira
"""

import numpy as np
import matplotlib.pyplot as plt

r = 3.6
dt = 0.5
N = 250

def F(x,r):
    return r*x*(1 - x)

t = np.arange(0,N, dt)
Nt = t.size
x = np.zeros(Nt)
r = np.array([2.5, 2.9, 3.1, 3.3, 3.44, 3.47, 3.5, 3.54, 3.55, 3.56, 3.568, 3.57, 3.6])
Nr = r.size
ults = np.zeros((Nr, 100))

x[0] = 0.3

for i in range (1, Nr):
    for n in range (1,Nt):
        x[n] = F(x[n-1], r[i-1])
    ults[i,:] = x[-101: -1]

for i in range(0,Nr-1):
    for j in range(0,99):
        plt.plot(r[i], ults[i,j], 'g.', markersize = 1.6)   
        plt.title("valores de x para cada r")

