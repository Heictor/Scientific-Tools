# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 18:06:39 2018

@author: heict
"""
#Used libraries.
import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
import pylab
from scipy.misc import derivative as deriv

#This block is responsable for asking to the user the needed initial data.
so=float(input('Insert the value of the initial position: '))
vo=float(input('Insert the value of the initial speed: '))
a=float(input('Insert the value of the initial acceleration: '))
print("\n")

#Defining the position of the object as a function of time.(Equation-1.0)
def S(t):
    return so+vo*t+0.5*a*t**2

t = sy.Symbol('t')
print("Result of the first derivative: ")
print(deriv(S, t))
print(sy.diff(S(t), t))
print("-----------------------------------\n")
print("Result of the second derivative: ")
print(deriv(S, t, n=2))
print(sy.diff(S(t), t, 2))
print("-----------------------------------\n")

#Defining the velocity of the object as the derivative of the first equation.(Equation-1.1)
def V(t):
    return deriv(S, t)

'''
The following structure solves the roots of both quadratic and linear equations
The results are contained inside these brackets "[]"
'''

print("Roots of the quadratic equation")
sy.solve(S(t))
print(sy.solve(S(t)))
print("-----------------------------------\n")
print("Roots of the linear equation")
sy.solve(V(t))
print(sy.solve(V(t)))
print("-----------------------------------\n")

tc1=-vo/a
Sc1=S(tc1)
print(tc1,Sc1)

#Using matplotlib to plot graphic of Uniform Linear Motion With Variable Velocity
t = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()
ax.plot(t, S(t), 'r', linewidth=2.0)
plt.axvline(color = 'black') #Vertical Line
plt.axhline(S(0), ls = '--') #Dashed Horizontal Line
ax.scatter(0, S(0), color='k', linewidth=4.0) #Black Dot
ax.annotate("Dot 0",
            xy=(0, S(0)),
            xycoords='data',
            xytext=(so+2,so),
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3")
            )
plt.grid()
plt.xlabel('Time(s)')
plt.ylabel('Positions(m)')
plt.title('Uniform Linear Motion With Variable Velocity')
pylab.legend(["Parabola"],loc=2)
plt.show()

tc2=-vo/a;
Sc2=V(tc2);
print(tc2,Sc2)

#Using matplotlib to plot graphic of Uniform Linear Motion With Constant Velocity
t = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()
ax.plot(t, V(t), 'r', linewidth=2.0)
plt.axvline(color = 'black') #Vertical Line
plt.axhline(V(0), ls = '--') #Dashed Horizontal Line
ax.scatter(0, V(0), color='k', linewidth=4.0) #Esse é o ponto preto
ax.annotate("Movement direction change",
            xy=(0, V(0)),
            xycoords='data',
            xytext=(3,0),
            arrowprops=dict(arrowstyle="->",connectionstyle="arc3")
            )
plt.grid()
plt.xlabel('Time(s)')
plt.ylabel('Velocity(m/s)')
plt.title('Uniform Linear Motion With Constant Velocity')
pylab.legend(["Straight Line"],loc=2)
plt.show()
