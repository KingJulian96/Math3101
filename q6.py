from numpy import linspace, empty, arange, vstack, ones, zeros
import q2, q3, q5, q4

def assemble_matrices(node, C, kappa, w, y):
    P = len(C[0])
    A = zeros((P+1, P+1))
    M = zeros((P+1, P+1))
    p = 1
    while(p <= P):
        elt = [node[p-1], node[p]]
        ap, mp = q2.elt_matrices(elt, kappa, w, y)
        j = 0
        while (j < 2):
            r = int (C[j][p-1])-1
            if r <= (P+1):
                k = 0
                while(k < 2):
                    s = int (C[k][p-1])-1
                    A[r,s]+= ap[j,k]
                    M[r,s]+= mp[j,k]
                    k+=1
            j+=1
        p+=1

    return A, M

def assemble_load_vector(node, C, f, w, y):
    P = len(C[0])
    f_vec = zeros(P+1)
    p = 1
    while(p <= P):
        elt = [node[p-1], node[p]]
        fp = q3.elt_load_vector(elt, f, w, y)
        j = 0
        while (j < 2):
            r = int (C[j][p-1])-1
            if r <= (P+1):
                f_vec[r]  += fp[j]
            j+=1
        p+=1

    return f_vec
