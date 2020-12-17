from numpy import linspace, empty, arange, vstack, ones

def elt_matrices(elt, kappa, w, y):
    hp = elt[1]- elt[0]
    Ap = empty ((2,2))
    Ap[0] = [1, -1]
    Ap[1] = [-1, 1]
    l = 0
    sum = 0
    while(l < len(w)):
        plp = elt[0] + (y[l]*hp)
        sum += w[l] * kappa(plp)* (plp**2)
        l+=1
    Ap = (Ap/hp)*(sum)

    Mp = empty ((2,2))
    j = 0
    while(j < 2):
        k = 0
        while(k < 2):
            l = 0
            sum = 0
            while (l < len(w)):
                plp = elt[0] + y[l]*hp
                sum += w[l]*psi(hp, elt, plp, k)* psi(hp, elt, plp, j)*(plp**2)
                l += 1
            Mp[j,k] = sum
            k += 1
        j += 1
    return Ap, Mp*hp

def psi(hp,elt, plp, flag):
    if (flag == 0):
        return (elt[1]-plp)/hp
    if (flag == 1):
        return (plp-elt[0])/hp
