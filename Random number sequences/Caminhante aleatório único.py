# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 10:53:12 2022

@author: Geraldo Siqueira
"""
import numpy as np
import matplotlib.pyplot as plt
import random

def Caminhada(x0, Nt, p):
    x = np.zeros(Nt)
    x[0] = x0
    random.seed(10)
    for k in range(1, Nt):
        r = random.uniform(0, 1)
        if r < p:
            x[k] = x[k-1] + 1
        else:
            x[k] = x[k-1] - 1
    return x

x = Caminhada(0, 50000, 0.5)
plt.plot(x)
plt.xlabel('tempo')
plt.ylabel('Posição')