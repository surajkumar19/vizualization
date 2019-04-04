# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 16:35:10 2018

@author: devar
"""


import matplotlib.pyplot as plt
import numpy as np
 
# create data
x = np.random.rand(15)
y = np.random.rand(15)
z = np.random.rand(15)
cool = np.random.rand(15)
 
# Change global size playing with s
plt.scatter(x, y, s=z*200, c = cool)
plt.savefig('Bubble_plot.svg',format = "svg",  dpi=96)
plt.show()
plt.clf()
