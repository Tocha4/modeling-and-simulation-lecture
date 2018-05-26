import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import time
from numba import jit



mat1 = 'Silber'
#%% Materialeigenschaften
material = {'PET': [0.24, 1.38, 1.5], 'Silber': [429, 10.49, 0.235]} # lambda, Dichte, spez.Wärmekapazität
mat = material[mat1]
a = mat[0] /(mat[1]*mat[2]*10**4)

#%% Geometrie und Diskretisierung
stab_x = 1 # [cm]
stab_y = 1 # [cm]
Zeitraum = 6 # [Sekunden]
dx = 0.01
dy = 0.01
dt = 0.0014

#%% Berechnung der Konstanten + Stabilität
C1 = a*dt/(dx**2)
C2 = a*dt/(dy**2)

stability = dt*a/(dx**2)

print('Stabilitätskriterium: {}'.format(stability))

#%% Simulation

T = np.zeros(shape=(int(stab_y/dy), int(stab_x/dx), int(Zeitraum/dt)), dtype=np.float64)

T[:,:,:] = 20
T[40:60,40:60,:] = 100


@jit(nopython=True)
def calc_T(T,C1,C2, const):
    for n in range(1,len(T[0,0,:])-1):
        T[40:60,40:60,n] = 100
        for j in range(1,len(T[0,:,0])-1):
            for i in range(1,len(T[:,0,0])-1):
                T[i,j,n+1] = C1*(T[i+1,j,n]-2*T[i,j,n]+T[i-1,j,n]) + C2*(T[i,j+1,n]-2*T[i,j,n]+T[i,j-1,n]) + T[i,j,n]
        T[:,0,n+1] = const + T[:,1,n+1]
        T[:,-1,n+1] = const + T[:,-2,n+1]
    return T

#%%
start = time.time()
T = calc_T(T, C1, C2, -1)
print('Time = {:.2f}'.format(time.time()-start))
#%%
x = np.arange(0, int(stab_x/dx), 1)
y = np.arange(0, int(stab_y/dy), 1)
X, Y = np.meshgrid(x, y)
levels = np.arange(20,100,5)


plt.figure()
n_imgs = 4
for count in range(1,n_imgs+1):
    plt.subplot(2,2,count)
    number = int(count/n_imgs*len(T[0,0,:]))-1
    print(number)
    plt.imshow(T[:,:,number], cmap='rainbow')
    plt.contour(X,Y,T[:,:,number], levels, linewidths=1, colors='k')
    plt.title('Time: {:.3f} Sekunden'.format(number/(len(T[0,0,:])-1)*Zeitraum))
    plt.xticks([])
    plt.yticks([])

plt.show()

#fig = plt.figure()
#m = 25
#for count in range(m):
#
#    number = int(count*len(T[0,0,:])/m)
#    print(number)
#    plt.plot(T[25,:,number], label='{}'.format(number))
#    plt.title('Time: {:.3f} Sekunden'.format(number/(len(T[0,0,:])-1)*Zeitraum))
#    plt.legend()
#
















