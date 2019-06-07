# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 21:09:49 2018

@author: heict
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#set plot sizes
plt.rcParams['figure.figsize'] = (10, 10)  # (width, height)
plt.rcParams['font.size'] = 10
plt.rcParams['legend.fontsize'] = 16

n=int(input('Insert the number of particles: ')) #Number of particles

m = np.random.randint(1,200, n)
print(m)

x = np.random.randint(0, 200, n)
print(x)

y = np.random.randint(0,200,n)
print(y)

z = np.random.randint(0,200,n)
print(z)

mcx = np.sum(x*m)/np.sum(m)
print('The center of mass in x is: ',mcx)

mcy = np.sum(y*m)/np.sum(m)
print('The center of mass in y is: ',mcy)

mcz = np.sum(z*m)/np.sum(m)
print('The center of mass in z is: ',mcz)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, s=m);
ax.scatter(mcx, mcy, mcz, color='k', marker='+', s=1e4);
plt.title('3 Dimensional Center of Gravity');
plt.show()