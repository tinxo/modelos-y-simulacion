#-*-coding:utf8;-*-
#Congruencias Aditivo
# paramA = 1
# paramC = 1

def generadorCongruenciasAditivo(v1, v2, paramK, paramM, cantidadGenerar):
    serie = []
    for x in range(paramK):
        v3 = (v1 + v2) % paramM
        serie.append(v3)
        v1 = v3
    while (len(serie) <= cantidadGenerar + paramK):
        v2 = serie[len(serie) - paramK]
        v3 = (v1 + v2) % paramM
        serie.append(v3)
        v1 = v3

    serieResultado = serie[paramK:]
    return serieResultado