"""
Created on Wed Nov 18 22:30:22 2020

@author: Andreas Mastronikolis

This is a project that computes the evolution of a
one-dimensional difference equation given an initial condition.
The script also reveals the associated Cobweb schematic.

"""

import matplotlib.pyplot as plt
import numpy as np

## -------------------------------------------------- ##

Initial_Condition = 0
Data_Points = 20

## -------------------------------------------------- ##

def Function(x):
    # The user can freely change the functional form of this function.
    return x**2 - 1

def X(n):
    ## This function is using recursion to output the n-th element of the sequence X.
    if (n == 0): # At n = 0, the sequence takes the value of the initial condition.
        return Initial_Condition
    elif (n > 0): # Else, for n > 0, the sequence is evalutated recursively.
        return Function(X(n-1))

Image = [] # This array collects the values of one-dimensional map.

for i in range(Data_Points): 
    # For all the data points the user wishes to plot,
    # We append the Image array with the i-th element of the Sequence.
    Image.append(X(i))
    
F_Domain = np.linspace(min(Image), max(Image), num = 1000) # This is the Domain of Function(x), for a given evolution of the sequence X.
    
# --------------- Plotting the Evolution of the Sequence ----------------------- #
    
fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (15,2.5))
ax.grid(alpha = 1)
ax.set_ylabel(r'$X_n$')
ax.set_xlabel(r'$n$')
ax.set_xticks(range(Data_Points))
ax.plot(range(Data_Points), Image, 'o-k', markersize = 5, mec = 'black', mfc = 'white')

# ------------------------------------------------------------------------------ #

# ------------------------------- Cobweb Plot ---------------------------------- #

fig1, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (10,8))
ax.grid()
ax.plot(F_Domain, Function(F_Domain), ls = '-', lw = 2, alpha = 0.8)
ax.plot(F_Domain, F_Domain, alpha = 0.4, lw = 2)
ax.set_xlabel(r'$X_n$')
ax.set_ylabel(r'$f(X_n)$')
ax.set_title('Cobweb Schematic', fontsize = 13)

P_X = []
P_Y = []

for i in range(Data_Points):
    if (i == 0):
        P_X.append(Initial_Condition)
        P_X.append(Initial_Condition)
        P_Y.append(0)
        P_Y.append(Function(Initial_Condition))
    else:
        P_X.append(X(i))
        P_X.append(X(i))
        P_Y.append(X(i))
        P_Y.append(Function(X(i)))
        
ax.plot(P_X, P_Y, 'o--r', markersize = 5, mec = 'black', mfc = 'green')
