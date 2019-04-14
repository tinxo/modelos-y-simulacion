#Fibonacci
def generadorFibonacci(v1, v2, ctrl, cantidadGenerar):    
    serie = []
    serie.append(v1)
    serie.append(v2)

    while (len(serie) <= cantidadGenerar):
        if ((v1 + v2) <= ctrl):
            v3 = v2 + v1 #k = 0
        else:
            v3 = v2 + v1 + ((-1) * ctrl)
        serie.append(v3)
        v1 = v2
        v2 = v3
    return serie