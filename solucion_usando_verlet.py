#!/usr/bin/env python
# -*- coding: utf-8 -*-

from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt


condicion_inicial = [10., 0., 0., 0.3]

p = Planeta(condicion_inicial)

n_pasos=4000
dt=0.1

X=np.zeros(n_pasos)
Y=np.zeros(n_pasos)
VX=np.zeros(n_pasos)
VY=np.zeros(n_pasos)
ET=np.zeros(n_pasos)
t_values=np.zeros(n_pasos)

X[0]=condicion_inicial[0]
Y[0]=condicion_inicial[1]
VX[0]=condicion_inicial[2]
VY[0]=condicion_inicial[3]
ET[0]=p.energia_total()

p.avanza_rk4(dt)
X[1]=p.y_actual[0]
Y[1]=p.y_actual[1]
VX[1]=p.y_actual[2]
VY[1]=p.y_actual[3]
ET[1]=p.energia_total()
t_values[1]=p.t_actual



for i in range(2,n_pasos):
    Y_anterior=np.array([X[i-2], Y[i-2], VX[i-2], VY[i-2]])
    p.avanza_verlet(dt,Y_anterior)
    X[i]=p.y_actual[0]
    Y[i]=p.y_actual[1]
    VX[i]=p.y_actual[2]
    VY[i]=p.y_actual[3]
    ET[i]=p.energia_total()
    t_values[i]=p.t_actual

fig=plt.figure(1)
plt.clf()
plt.subplot(2, 1, 1)
fig.subplots_adjust(hspace=.5)
plt.plot(X , Y,)
plt.title("Trayectoria")
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(2, 1, 2)
plt.plot(t_values,ET)
plt.xlabel("Tiempo [s]")
plt.ylabel("Energia [J]")
plt.savefig('Sol_Verlet.eps')
plt.show()
plt.draw()
