# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 09:52:57 2022

@author: Geraldo Siqueira
"""
import numpy as np
import matplotlib.pyplot as plt

N = 1000000
mi = 1
sigma = 2
x = np.random.normal(mi,sigma,N)
x_axis = np.arange(-7.5, 10, 0.001)
Pteorico = (1/(np.sqrt(2*np.pi)*sigma))*np.exp(-(1/2)*((x_axis-mi)**2)/sigma**2)
media = 0
var = 0

#Mostrar o valor médio e o desvio padrão da sequencia e o desvio padrão da média teórico
print(np.mean(x), np.std(x), 1/np.sqrt(N))

for n in range (0,N-1):
    media += x[n]
media = media/N
for n in range (0,N-1):
    var += (x[n] - media)**2
var = var/N
desvio = np.sqrt(var)

print(media, desvio)
'''
fig, (ax1, ax2) = plt.subplots(1, 2, figsize =(15,5))

#plota os valores de x na ordem que foram escolhidos
ax1.plot(x, ',', color = 'blue', alpha = 0.05)
ax1.set_xlabel(r'$n$'), ax1.set_ylabel(r'$x$');

#constrói o histograma de todos os elementos de x
ax1.hist(x, 50, color = 'green', density = 'true') #distribui os elementos de x em 50 caixas
ax1.set_xlabel(r'$x$'), ax1.set_ylabel('Frequência');

#plotando a curva teórica
ax2.plot(x_axis, norm.pdf(x_axis,1,2))
ax2.set_xlabel(r'$x$'), ax2.set_ylabel('Frequência');
ax2.set_ylim([0,0.6])
ax2.set_xlim([-1, 1])
'''
plt.hist(x, 50, color = 'blue', density = 'true')
plt.plot(x_axis, Pteorico, color = 'r')
plt.xlabel(r'$x$'), plt.ylabel('Densidade de probabilidade')
