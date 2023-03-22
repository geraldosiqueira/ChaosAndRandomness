# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 13:58:37 2022

@author: Geraldo Siqueira   
"""

import numpy as np
import matplotlib.pyplot as plt

r = 3.73
dt = 1
N = 550

def F(x,r):
    return r*x*(1 - x)

def f(x,r):
    return r -  2*x*r

t = np.arange(0,N, dt)
Nt = t.size
x = np.zeros(Nt)
r = np.linspace(2.8, 4.0, num=1000)
Nr = r.size
lamb = np.zeros(Nr)


x[0] = 0.1

for i in range (0,Nr):    
    for n in range (1,Nt):
        x[n] = F(x[n-1], r[i])
    f_linha = f(x, r[i])
    lamb[i] = (1/N)*sum(np.log(np.abs(f_linha)))

#Determinando onde o λ é maior:
print((max(lamb)))
for i in range (1,Nr-1):    
    if lamb[i] == 0.6929186132855552:
        print(i)    
print(r[999])
print(lamb[998], lamb[999])

plt.title("λ para cada r")
plt.plot(r, lamb, color = 'orange' , marker = '')
plt.plot([2.8,4], [0,0], 'b-')
