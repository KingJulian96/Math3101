from numpy import linspace, empty, ones, zeros, dot, divide, sum, array
import q2, q3, q5, q4, q6, q8
import math
from math import e
from numpy import loadtxt
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

Gauss8 = loadtxt("Gauss8.txt")

def kappa(x):
    return 0.5

def f(rho, t):
    if (0 <= t):
        if (t <= T/2):
            return 20*(math.exp(-4*(rho**2)))
    return 0

T = 2.5

time = linspace(0.25, 2.5, 10)


def fig2(U, Ubar, node, t):
    fig = plt.figure()
    ax = plt.subplot(111)
    i = 0
    while i  < (P+1):
        if(node[i] == 0 or node[i] == 0.5 or node[i] == 1.0):
            temp = r'$\rho$'+' = '+  str(node[i])
            ax.plot(t, U[:,i], label = temp)
        i+=1
    ax.plot(t, Ubar, label = "spatial average", linestyle="--")
    plt.xlabel(r'$t$')
    plt.ylabel(r'$u$')
    ax.legend()
    plt.grid(True)
    plt.show()

def cooling_down(U, Ubar, node, t):
    fig = plt.figure()
    ax = plt.subplot(111)
    i= 0
    while i <(N+1):
        if (t[i] in time):
            if (t[i] > 2.5/2):
                temp = 't = '+  str(t[i])
                ax.plot(node, array(U).T[:,i], label = temp)
        i+=1
    plt.xlabel(r'$\rho$')
    plt.ylabel(r'$u$')
    ax.legend()
    plt.grid(True)
    plt.show()

def heating_up(U, Ubar, node, t):
    fig = plt.figure()
    ax = plt.subplot(111)
    i= 0
    while i <(N+1):
        if (t[i] in time):
            if (t[i] <= 2.5/2):
                temp = 't = '+  str(t[i])
                ax.plot(node, array(U).T[:,i], label = temp)
        i+=1
    plt.xlabel(r'$\rho$')
    plt.ylabel(r'$u$')
    ax.legend()
    plt.grid(True)
    plt.show()
if __name__ == '__main__':
     #print (t)
     #print (Gauss8)
    w, y = q4.readfile()
    P = 30
    N = 900
    U, Ubar, node, t = q8.backward_Euler(P, N, T, kappa, f, w, y)
    fig2(U, Ubar, node, t)
    heating_up(U, Ubar, node, t)
    cooling_down(U, Ubar, node, t)
