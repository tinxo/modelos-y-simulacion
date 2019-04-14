#-*-coding:utf8;-*-
#Congruencias Multiplicativo
# paramC = 0
# paramK = no se utiliza
# v2 = no se utiliza

def generadorCongruenciasMultiplicativo(v1, paramA, paramM, cantidadGenerar):
    serie = []
    while (len(serie) <= cantidadGenerar):
        v3 = (paramA * v1) % paramM
        serie.append(v3)
        v1 = v3
    return serie