from numpy import linspace, empty, ones, zeros, dot, divide, sum
import q2, q3, q5, q4, q6
import math
from math import e
from scipy.sparse.linalg import factorized
from scipy.linalg import solve_banded
from scipy.sparse import coo_matrix, csc_matrix


def backward_Euler(P, N, T, kappa, f, w, y):
    U = zeros((N+1,P+1))
    Ubar= ones(N+1)
    dt = T/N
    node, t, C = q5.grid_points(P, N, T)
    A,M = q6.assemble_matrices(node, C, kappa, w, y)

    A[P,P]+=1
    LHS = (M + dt*(A))
    U[0] = ones(P+1)
    LHS = (M+dt*(A))
    LHS =csc_matrix(LHS)
    direct_solver = factorized(LHS)
    n = 1
    while (n < N+1):
        f_vec= q6.assemble_load_vector(node, C, lambda x: f(x, t[n]), w, y)
        f_vec[P] +=1
        RHS = dot(M, U[n-1,:]) + dt*f_vec
        U[n,:] = direct_solver(RHS)
        Ubar[n] =sum (3*dot(M, U[n,:]))
        n+=1

    return U, Ubar, node, t


if __name__ == '__main__':
    w, y = q4.readfile()
    T = 2.5
    P = 5
    N = 10
    U, Ubar, node, t = backward_Euler(P, N, T, kappa, f, w, y)
    print (Ubar)
