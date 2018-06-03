import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(a,t,k,k2,n,m):
#    dadt = k*a**1*(1-a)**3
    dadt = (k+k2*a**m)*(1-a)**n
    return dadt

def k1_f(T):
    a = 4.33
    E = 24.1
    R = 8.31448/1000
    k = a*np.exp(-E/(R*T))
    return k

def k2_f(T):
    a = 1.41e+10
    E = 64.3
    R = 8.31448/1000
    k = a*np.exp(-E/(R*T))
    return k


def comp_n(amount):
    y0 = 0
    
    t = np.linspace(0,600,1000)
    
    
    for T in range(270,300,5):
        a = odeint(model, y0, t, args=(k1_f(T), k2_f(T), 3.56, 0.99))
        
        #dadt = model(a,t)
        
        dadt = np.gradient(a[:,0], t)
        
        plt.subplot(2,1,1)
        plt.plot(t,a, label=T)
        plt.ylabel(r'Reaktionsumsatz $\alpha$', fontsize=12)
        plt.xlabel('Time [sec]', fontsize=12)
#        plt.legend()
        
        plt.subplot(2,1,2)
        plt.plot(t,dadt, label=T)
        plt.ylabel(r'Reaktionsgeschwindigkeit $\dfrac{\partial\alpha}{\partial t}$ $[sec^{-1}]$', fontsize=12)
        plt.xlabel('Time [sec]', fontsize=12)
#        plt.legend()
        
    
    
    mat1 = 'Duromer'
    material = {'Duromer': [0.2, 1.2, 1.5]} # Wärmeleitfähigkeit, Dichte, spez. Wärmekapazität
    mat = material[mat1]
    time = 300 # Zeit [sec]
    dt = 0.25 # Zeitschritt [sec]
    Hr = 2 # Reaktionsenthalpie [J/mol]
    n = amount # Stoffmenge [mol]
    qt = Hr*n # Gesamte freigesetzte Wärme [J]
    Cq = qt*dt/(mat[1]*mat[2])
    
    for T_s in range(270,300,5):
        
        T = np.zeros(int(time/dt))
        T[0] = T_s
        a = [0]
        dt_a = np.linspace(0,dt,100)
        
        dadt_points = []
        a_points = []
        for n in range(len(T)-1):
            
            a = odeint(model, a[-1], dt_a, args=(k1_f(T[n]), k2_f(T[n]), 3.56, 0.99))
            dadt = np.gradient(a[:,0], dt_a)
            dadt_points.append(dadt[-1])
            a_points.append(a[-1])
            
            T[n+1] = dadt[-1]*Cq + T[n]
        
        plt.subplot(2,1,1)
        t = np.linspace(0,time,len(T)-1)
        plt.plot(t, a_points, '--', label=amount)
        plt.legend()
        
        plt.subplot(2,1,2)
        plt.plot(t, dadt_points, '--',label=amount)
        plt.legend()
        
    
    