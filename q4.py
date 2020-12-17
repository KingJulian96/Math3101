from numpy import linspace, empty, arange, vstack, ones
import math
import q2, q3
from math import e
pi = math.pi
elt = [0.5, 1.0]
def kappa(p):
    return (math.exp(-p))

def f(p):
    return math.sin(math.pi*p)


def readfile():
    f =  open("Gauss8.txt", "r")
    w = []
    y = []
    for x in f:
        line = x.split()
        w.append(float(line[0]))
        y.append(float(line[1]))
    return w, y


def test_elt_matvec():
    w, y = readfile()
    ap, mp = q2.elt_matrices(elt, kappa, w, y)
    fp = q3.elt_load_vector(elt, f, w, y)
    print ("Ap is ________________________")
    print (ap)
    print ("Mp is ________________________")
    print (mp)
    print ("fp is ________________________")
    print (fp)

if __name__ == '__main__':
    test_elt_matvec()
