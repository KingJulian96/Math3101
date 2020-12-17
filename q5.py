from numpy import linspace, empty, arange, vstack, ones

def grid_points(P, N, T):
    node = linspace(0,1,P+1)
    dt = T/N
    t = dt * linspace(0,N,N+1)
    C = empty ((2,P))
    C[0] = linspace(1,P,P)
    C[1] = linspace(2,P+1,P)
    return node, t, C

if __name__ == '__main__':
    print (grid_points(5,8,2))
