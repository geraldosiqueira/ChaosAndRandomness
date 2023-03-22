# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 08:56:16 2022

@author: Geraldo Siqueira
"""

import numpy as np
import matplotlib.pyplot as plt

N = 1000000
x = np.random.normal(1,2,N)

#Mostrar o valor médio e o desvio padrão da sequencia e o desvio padrão da média teórico
print(np.mean(x), np. std(x), 1/np.sqrt(N))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize =(15,5))

#plota os valores de x na ordem que foram escolhidos
ax1.plot(x, ',', color = 'blue', alpha = 0.05)
ax1.set_xlabel(r'$n$'), ax1.set_ylabel(r'$x$');

#constrói o histograma de todos os elementos de x
ax2.hist(x, 50, color = 'green') #distribui os elementos de x em 50 caixas
ax2.set_xlabel(r'$x$'), ax2.set_ylabel('Frequência');
