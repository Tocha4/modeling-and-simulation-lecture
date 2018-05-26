#%% Bibliotheken importieren
import numpy as np
import matplotlib.pyplot as plt
import time

#%% Materialeigenschaften
mat = 'Silber'
material = {'PET': [0.24, 1.38, 1.5], 'Silber': [429, 10.49, 0.235]}

mat = material[mat]
a = mat[0]/(mat[1]*mat[2]*10**4)
#%% Geometrie und Diskretisierung
stab = 5 # cm0
Zeitraum = 20 # sec
dx = 0.01
dt = 0.0025
#%% Berechnung der Konstanten + Stabilität
C = a*dt/dx**2
stability = dt*a/dx**2


#%% Simulation
simT = np.zeros(shape=(int(Zeitraum/dt), int(stab/dx)))

simT[0, :] = 20
simT[:, 0] = 100
simT[:, -1] = 100

for n in np.arange(0,len(simT[0:,1])-1, 1):
    for i in np.arange(1,len(simT[0,0:])-1,1):
        simT[n+1, i] = C*(simT[n,i+1] - 2*simT[n,i] + simT[n,i-1]) + simT[n,i]


#%% Plot
plt.figure()
for m in np.arange(0,len(simT[0:,1]),1000):
    plt.plot(np.arange(0,int(stab//dx),1)*dx, simT[m])
    
plt.grid()
plt.title(mat)
plt.xlabel('Stablänge [Zentimeter]')
plt.ylabel('Temperatur [°C]')


#%% Save




#%% 2D Plot




