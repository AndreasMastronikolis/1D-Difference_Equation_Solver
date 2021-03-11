"""
Created on Wed Nov 18 22:30:22 2020

@author: Andreas Mastronikolis

This is a project that computes the plot of the evolution of a
one-dimensional difference equation of the form X_{n+1} = F(X_n)
given an initial condition. The script also reveals the associated Cobweb schematic.

"""

import matplotlib.pyplot as plt
import numpy as np

## -------------------------------------------------- ##

Initial_Condition = 0.5 # This variable stores the initial condition of the sequence; that is, X_0.
Data_Points = 20 # This variable stores the amount of data points the user wishes to plot.

## -------------------------------------------------- ##

def Function(x):
    # This is the function F; defined above. The user can freely change the functional form of this function.
    return x**2 - 1

def X(n):
    ## This function is using recursion to output the n-th element of the sequence X.
    if (n == 0): # At n = 0, the sequence takes the value of the initial condition.
        return Initial_Condition
    elif (n > 0): # Else, for n > 0, the sequence is evalutated recursively.
        return Function(X(n-1))

Image = [] # This array collects the values of Sequence X(n) for a pre-specified value of Data_Points.

for i in range(Data_Points): 
    # For all the data points the user wishes to plot,
    # We append the Image array with the i-th element of the Sequence; from i = 0 to i = Data_Points
    Image.append(X(i))
    
F_Domain = np.linspace(min(Image), max(Image), num = 1000) # This is the Domain of Function(x), for a given evolution of the sequence X.
    
# --------------- Plotting the Evolution of the Sequence ----------------------- #
    
fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (15,5))
ax.grid(alpha = 0.5, color = 'black')
ax.set_ylabel(r'$X_n$', fontsize = 13)
ax.set_title(r'Evolution of the Sequence $X_n$ as a function of $n$')
ax.set_xlabel(r'$n$', fontsize = 13)
ax.set_xticks(range(Data_Points))
ax.plot(range(Data_Points), Image, 's-.k', markersize = 7, mec = 'black', mfc = 'orange', alpha = 0.6)

# ------------------------------------------------------------------------------ #

# ------------------------------- Cobweb Plot ---------------------------------- #

fig1, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (10,8))
ax.grid()
ax.plot(F_Domain, Function(F_Domain), ls = '-.', lw = 2, alpha = 0.5)
ax.plot(F_Domain, F_Domain, alpha = 0.4, lw = 2)
ax.set_xlabel(r'$X_n$')
ax.set_ylabel(r'$f(X_n)$')
ax.set_title('Cobweb Schematic', fontsize = 13)

P_X = [] # This array collects all the x-coordinates of the points in the Cobweb plot.
P_Y = [] # This array collects all the y-coordinates of the points in the Cobweb plot.

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
