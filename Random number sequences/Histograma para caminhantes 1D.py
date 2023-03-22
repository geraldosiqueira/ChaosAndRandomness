# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:10:54 2022

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

def Histograma (x, #matriz com N caminhantes (linhas) em Nt instentes (colunas)
                t, #coluna da matriz em que se deseja construir o histograma
                Nhist, #número de caixas que você deseja para o seu histograma
                a, #inicio do intervalo desejado
                b, #fim do intervalo desejado
                ):
   Dx = (b - a) / Nhist
   Xh = np.arange(a, b+Dx, Dx); # vetor que guarda as posições das caixas
   N = np.size(x[:,t]) # no. de elementos em cada coluna de x
   hist = np.zeros(Nhist+1) # inicializando o histograma
   for n in range(N):
       y = x[n,t] - a
       Ncaixa = int(Nhist*(y/(b-a)))
       if 0 <= Ncaixa < Nhist+1:
           hist[Ncaixa] += 1
   hist = hist/(N*Dx) # normaliza o histograma --> Distr. de Prob.
   return Xh, hist


NC, Nt = 10000, 500
x = Caminhada(0, NC, Nt, 0.5)
'''
for n in range(0, NC, NC//100):
    plt.plot(x[n, :])
plt.xlabel('tempo')
plt.ylabel('Posição')
'''

pos, y = Histograma(x, 10, 10, -10, 10)
plt.plot(pos, y)
pos, y = Histograma(x, 20, 10, -10, 10)
plt.plot(pos, y)
pos, y = Histograma(x, 50, 10, -10, 10)
plt.plot(pos, y)
pos, y = Histograma(x, 100, 10, -10, 10)
plt.plot(pos, y)
pos, y = Histograma(x, 200, 10, -10, 10)
plt.plot(pos, y)
pos, y = Histograma(x, 400, 10, -10, 10)
plt.plot(pos, y)