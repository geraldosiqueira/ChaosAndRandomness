# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 13:12:26 2022

@author: geral
"""


import numpy as np
import matplotlib.pyplot as plt
import random
from numba import jit

@jit
def Histograma(x, t, Nhist, a, b):
    x_aux = []
    for k in range( np.size(x[t,:])):
        if x[t,k] >= a and x[t,k] <= b:
            x_aux.append(x[t,k])
        
    dx = (b-a)/Nhist
    Xh = np.arange(a, b, dx)
    Hist = np.zeros(Nhist)
    N = np.size(x_aux)
    for i in range(N):
        j = int((x_aux[i] - a)/dx)
        if j<Nhist and j>0:
            Hist[j] += 1
    Hist = Hist/(N*dx)
    return Xh, Hist

@jit
def Caminhada2D(x0, y0, N, Nt, p):
    x = np.zeros( [Nt, N] )
    y = np.zeros( [Nt, N] )
    x[:, 0] = x0
    y[:, 0] = y0
    np.random.seed(7)
    for n in range(1, Nt):
        for i in range(N):
            r = random.uniform(0, 1)
            if r < p:
                x[n, i] = x[n-1, i] + 1
                y[n, i] = y[n-1, i]
            elif r < 2*p:
                x[n, i] = x[n-1, i] - 1
                y[n, i] = y[n-1, i]
            elif r < 3*p:
                x[n, i] = x[n-1, i]
                y[n, i] = y[n-1, i] + 1
            else:
                x[n, i] = x[n-1, i]
                y[n, i] = y[n-1, i] - 1
    return x, y

NC, Nt = 10000, 500
x, y = Caminhada2D(0, 0, NC, Nt, 0.25)

for tempo in [10, 20, 50, 100, 200, 400]:
    Xh, hist = Histograma(y, tempo, 60, -60,     60)
    plt.plot(Xh, hist)

plt.title('Eixo Y')
plt.xlabel('Posição dos caminhantes')
plt.ylabel('Densidade de probabilidade')