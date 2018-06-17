import numpy as np
import matplotlib.pyplot as plt

# Parameters
nx = 50
ny = 50
nt  = 100
xmin = 0
xmax = 2
ymin = 0
ymax = 1

K = 1e-8
µ = 0.001
print(K/µ)

dx = (xmax - xmin) / (nx - 1)
dy = (ymax - ymin) / (ny - 1)

# Initialization
dp = 0.8
rho  = np.zeros((ny, nx))
rho[:,:10] = 1
rho[0,:20] = 1
x  = np.linspace(xmin, xmax, nx)
y  = np.linspace(xmin, xmax, ny)
u = np.zeros((ny,nx))
v = np.zeros((ny,nx))


u_n = np.array([K/µ*dp/np.sum(rho,axis=1)])
u = np.repeat(u_n,(50),axis=1).reshape((50,50))
plt.imshow(u)
plt.colorbar()
