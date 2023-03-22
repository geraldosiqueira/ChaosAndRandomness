# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:02:49 2022

@author: Geraldo Siqueira
"""

import numpy as np
import matplotlib.pyplot as plt

def Caminhada(x0, N, Nt, p):
    x = np.zeros( [N, Nt] )
    x[:, 0] = x0
    np.random.seed(10)
    for n in range(1, Nt):
        r = np.random.random(N)
        s = np.where(r < p, 1, -1)
        x[:, n] = x[:, n-1] + s
    return x

NC, Nt = 10000, 500
x = Caminhada(0, NC, Nt, 0.5)
for n in range(0, NC, NC//100):
    plt.plot(x[n, :])
plt.xlabel('tempo')
plt.ylabel('Posição')