import numpy as np
import matplotlib.pyplot as plt


def velocity(K,nu,dp,rho,dx):
    
    u = K/nu*dp/(np.sum(rho)*dx)
    return u


K = 1e-11 # m²
nu = 0.1 # mPas
dp = 80000 # Pa

length = 0.2 # m
time = 120 # sec

dx = 0.001 # m
dt = 0.01 # sec

rho = np.zeros((int(time/dt), int(length/dx))) # Normierte Füllmenge 
rho[:,0] = 1 # Randbedingung



for n in range(len(rho[:,0])-2):
    u = velocity(K,nu,dp,rho[n],dx)
    stability = u*dt/dx
    print(stability)
    for i in range(1,len(rho[0,:])-1):
        
        rho[n+1,i] = rho[n,i] - stability*(rho[n,i]-rho[n,i-1])
        
        
g = 10
for m in range(g):
    c = int(len(rho[:,0])/g)-1
    
    plt.plot(rho[c*m], label=c*m)
    
plt.legend()