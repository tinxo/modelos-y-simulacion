#-*-coding:utf8;-*-
#Congruencias Mixto
# paramK = no se utiliza
# v2 = no se utiliza

def generadorCongruenciasMixto(v1, paramA, paramC, paramM, cantidadGenerar):
    serie = []
    while (len(serie) <= cantidadGenerar):
        v3 = (paramA * v1 + paramC) % paramM
        serie.append(v3)
        v1 = v3

    return serie