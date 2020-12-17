from numpy import linspace, empty, arange, vstack, ones, zeros
import q2, q3, q5, q4, q6

def kappa(x):
    return 1

def f(x):
    return 1

if __name__ == '__main__':
    P = 5
    w, y = q4.readfile()
    node, t, C = q5.grid_points(P, 1, 1)

    f_vec = q6.assemble_load_vector(node, C, f, w, y)
    A, M= q6.assemble_matrices(node, C, kappa, w, y)
    print ("matrix A is :")
    print (A)
    print ('---------------------------------')
    print ("matrix M is :")
    print (M)
    print ('---------------------------------')
    print ("matrix f_vec is :")
    print (f_vec)
