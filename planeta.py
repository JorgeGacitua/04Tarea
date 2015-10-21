#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Planeta(object):
    G=1
    M=1
    m=1
    '''
    Complete el docstring.
    '''

    def __init__(self, condicion_inicial, alpha=0):
        '''
        __init__ es un método especial que se usa para inicializar las
        instancias de una clase.

        Ej. de uso:
        >> mercurio = Planeta([x0, y0, vx0, vy0])
        >> print(mercurio.alpha)
        >> 0.
        '''
        self.y_actual = condicion_inicial
        self.t_actual = 0.
        self.alpha = alpha

    def ecuacion_de_movimiento(self):
        '''
        Implementa la ecuación de movimiento, como sistema de ecuaciónes de
        primer orden.
        '''
        x, y, vx, vy = self.y_actual

        rr= x**2 + y**2
        f_comun=(2 * self.alpha) / (rr**2) - 1 / ( np.sqrt(rr)**3 )
        fx = x * G * M * f_comun
        fy = y * G * M * f_comun
        return [vx, vy, fx, fy]


    def avanza_euler(self, dt):
        '''
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de Euler explícito. El
        método no retorna nada, pero re-setea los valores de self.y_actual.
        '''
        y_anterior=self.y_actual
        self.y_actual= y_anterior + dt*self.ecuacion_de_movimiento()
        self.t_actual+=dt


    def avanza_rk4(self, dt):
        '''
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de Runge Kutta 4. El
        método no retorna nada, pero re-setea los valores de self.y_actual.
        '''
        y_anterior=self.y_actual
        k1=self.ecuacion_de_movimiento()
        self.y_actual=y_anterior+(dt / 2) * k1

        k2=self.ecuacion_de_movimiento()
        self.y_actual=y_anterior+(dt / 2) * k2

        k3=self.ecuacion_de_movimiento()
        self.y_actual=y_anterior+(dt / 2) * k3

        k4=self.ecuacion_de_movimiento()

        self.y_actual=y_anterior + ( 1 / 6 )*(k1 + k2 + k3 + k4)

        self.t_actual+=dt


    def avanza_verlet(self, dt, Y):
        '''
        Similar a avanza_euler, pero usando Verlet.
        '''
        self.y_actual=2 * self.y_actual - Y + dt**2 * self.ecuacion_de_movimiento
        self.t_actual+=dt

    def energia_total(self):
        '''
        Calcula la energía total por del sistema en las condiciones actuales.
        '''
        x,y,vx,vy = self.y_actual
        K=m*0.5*(xv**2 + vy**2)
        r=np.sqrt(x**2+y**2)
        U=-G*M*m/r + self.alpha*G*M*m/r**2
