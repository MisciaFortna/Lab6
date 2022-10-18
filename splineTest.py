import speRead as sp
import scipy.interpolate as inter
import numpy as np
import pylab as plt
import sys

fileName = sys.argv[1]
y = sp.spread(fileName)
y = y[:2001]
x = []
for i in range(len(y)):
    x.append(i)

s1 = inter.UnivariateSpline(x, y, s=10)
plt.plot(x, s1, 'r-', label='Spline')
plt.legend()
plt.xlabel('channels')
plt.ylabel('counts')
plt.savefig('testIMG')
