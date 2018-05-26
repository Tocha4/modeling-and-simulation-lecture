import numpy as np
import matplotlib.pyplot as plt
import time


mat1 = 'PET'
#%% Materialeigenschaften
material = {'PET': [0.24, 1.38, 1.5], 'Silber': [429, 10.49, 0.235]} # lambda, Dichte, spez.Wärmekapazität
mat = material[mat1]
a = mat[0] /(mat[1]*mat[2]*10**4)

#%% Geometrie und Diskretisierung
stab = 5 # [Zentimeter]
Zeitraum = 20 # [Sekunden]
dx = 0.01
dt = 0.0025

#%% Berechnung der Konstanten + Stabilität
C = a*dt/dx**2

stability = dt*a/dx**2

print('Stabilitätskriterium: {}'.format(stability))

#%% Simulation
simT = np.zeros([int(Zeitraum//dt), int(stab//dx)])

simT[0, 0:] = 20
simT[1: , 0] = 100 # Navigation durch die Matrix
simT[1: , -1] = 100

g = 0
t = time.time()
for n in np.arange(0,len(simT[0:,1])-1,1):
    for i in np.arange(1,len(simT[0,0:])-1,1):
        simT[n+1,i] = C*(simT[n,i+1] - 2*simT[n,i] + simT[n,i-1]) + simT[n,i]
        g = g + 1
#    print(simT[n])
t = time.time() - t
print('Für die Berechnung der {} Punkte wurden {} Sekunden benötig '.format(g, t))

#%% Plot
plt.figure()
for m in np.arange(0,len(simT[0:,1]),1000):
    plt.plot(np.arange(0,int(stab//dx),1)*dx, simT[m])
    
plt.grid()
plt.title(mat1)
plt.xlabel('Stablänge [Zentimeter]')
plt.ylabel('Temperatur [°C]')

#%% Save

np.save(mat1, simT)

#%% 2D Plot

A = np.array([simT[i] for i in np.arange(0,len(simT[:,0]),len(simT[:,0])//800)])
plt.figure()
plt.imshow(A)
plt.colorbar()
