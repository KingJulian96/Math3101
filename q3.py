from numpy import linspace, empty, arange, vstack, ones

def elt_load_vector(elt, f, w, y):
    fp = empty (2)
    hp = elt[1]- elt[0]

    j = 0
    while (j < 2):
        sum = 0
        l = 0
        while (l < len(w)):
            plp = elt[0] + (y[l]*hp)
            sum += w[l]*f(plp)*psi(hp,elt, plp, j)*(plp**2)
            l += 1
        fp[j] = sum
        j+=1

    return fp*hp

def psi(hp,elt, plp, flag):
    if (flag == 0):
        return (elt[1]-plp)/hp
    if (flag == 1):
        return (plp-elt[0])/hp
