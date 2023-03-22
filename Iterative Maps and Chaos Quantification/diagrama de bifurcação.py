# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 11:14:47 2022

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
r = np.linspace(3.630, 3.635, num=1000)
Nr = r.size
ults = np.zeros((Nr, 100))

x[0] = 0.3

for i in range (1, Nr):
    for n in range (1,Nt):
        x[n] = F(x[n-1], r[i-1])
    ults[i,:] = x[-101: -1]

for i in range(0,Nr-1):
    for j in range(0,99):
        plt.plot(r[i], ults[i,j], 'g,')   
        plt.title("valores de x para cada r")