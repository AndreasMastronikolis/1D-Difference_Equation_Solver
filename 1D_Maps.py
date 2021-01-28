import matplotlib.pyplot as plt
import numpy as np

Initial_Condition = 1/7
Maximal_Limit = 20
r = 4

def f(x):
    return x**2 - 1

def D_Map(n):
    if (n == 0):
        return Initial_Condition
    elif (n > 0):
        return f(D_Map(n-1))

Image = []

for i in range(Maximal_Limit):
    Image.append(D_Map(i))
    
fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (15,2.5))
ax.grid(alpha = 1)
ax.set_xticks(range(Maximal_Limit))
ax.plot(range(Maximal_Limit), Image, 'o-k', markersize = 5, mec = 'black', mfc = 'white')
F_Domain = np.linspace(min(Image), max(Image), num = 1000)

fig1, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (10,8))
ax.grid()
ax.plot(F_Domain, f(F_Domain), ls = '-', lw = 2, alpha = 0.8)
ax.plot(F_Domain, F_Domain, alpha = 0.4, lw = 2)
ax.set_xlabel(r'$X_n$')
ax.set_ylabel(r'$f(X_n)$')
ax.set_title('Cobweb Schematic', fontsize = 13)

P_X = []
P_Y = []

for i in range(Maximal_Limit):
    if (i == 0):
        P_X.append(Initial_Condition)
        P_X.append(Initial_Condition)
        P_Y.append(0)
        P_Y.append(f(Initial_Condition))
    else:
        P_X.append(D_Map(i))
        P_X.append(D_Map(i))
        P_Y.append(D_Map(i))
        P_Y.append(f(D_Map(i)))
        
ax.plot(P_X, P_Y, 'o--r', markersize = 5, mec = 'black', mfc = 'green')