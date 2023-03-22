# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 14:20:20 2022

@author: Geraldo Siqueira
"""

import numpy as np
import matplotlib.pyplot as plt
import random
from numba import jit
import statsmodels.api as sm

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

NC, Nt = 1000, 100
Nt1 = np.arange(10, 100, 10)
Dx2 = np.zeros(NC)
Dx2Nt = np.zeros(9)
mdx2 = np.zeros(NC//2)
x, y = Caminhada2D(0, 0, NC, Nt, 0.25)

'''
#cálculo de (DeltaX)^2
for n in range (1,NC):
    x, y = Caminhada2D(0, 0, n, Nt, 0.25)
    Dx2[n]   = np.mean(x[Nt-1, :]**2) - (np.mean(x[Nt-1, :]))**2
    #Dx2[n]   = np.mean((x[Nt-1, :] - np.mean(x[Nt-1, :]))**2)
'''
#calculo da variancia em funçaõ de Nt
for i in range (1,10):
    Dx2Nt[i-1]   = np.mean(x[10*i-1, :]**2) - (np.mean(x[10*i-1, :]))**2

Y = Dx2Nt
X = Nt1
X = sm.add_constant(X)
model = sm.OLS(Y,X)
results = model.fit()
conf_ang = results.params[1]
conf_lin = results.params[0]

for i in range (NC//2):
    mdx2[i] = Dx2[(NC//2)+i]

print(np.mean(mdx2))
plt.plot(Nt1, conf_ang*Nt1 + conf_lin, 'r')
plt.plot(Nt1, Dx2Nt, 'b.')
#for n in range(0, NC, NC//100):
    #plt.plot(x[n, :], y[n, :])
    
#plt.plot(x,y)
plt.xlabel('Nt')
plt.ylabel('Variância')