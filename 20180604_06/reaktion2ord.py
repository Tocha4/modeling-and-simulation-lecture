import numpy as np
import matplotlib.pyplot as plt


k = 0.85
t = np.linspace(0,5)

A0 = 1

A = 1/(k*t+1/A0)

rho = 1
cp =1.5

U = (A0-A)/A0



q = np.diff(U)/np.diff(t)


plt.plot(t,A,'o--r', label='Konzentration A')
plt.plot(t,U, '*b', label='Umsatz')
plt.plot(t[1:],q,'g', label='Quelle')
plt.legend()
plt.show()