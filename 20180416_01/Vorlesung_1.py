import numpy as np
import keyword
import matplotlib.pyplot as plt

kw = keyword.kwlist
a = [2,3,5]
b = [a,a,a]
c = a+a

#print(a, b)
d = (2,4,6)
a[2] = 999
print(a[2], d[2])

e = np.array(a)
print(e*e)
f = np.array([1,2,3,4,5,6])

g = np.linspace(stop=10, start=1, num=200)
h = g*np.pi

plt.plot(g,h)