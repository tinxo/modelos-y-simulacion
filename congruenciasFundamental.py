#-*-coding:utf8;-*-
#Congruencias Fundamental
def generadorCongruenciasFundamental(v1, v2, paramA, paramC, paramK, paramM, cantidadGenerar):
    serie = []
    # Se generan los K primeros digitos que después se van a descartar
    for x in range(paramK):
        v3 = (paramA * v1 + paramC * v2) % paramM
        serie.append(v3)
        v1 = v3
    
    # Se hace la generación que en realidad se va a usar
    while (len(serie) <= cantidadGenerar + paramK):
        v2 = serie[len(serie) - paramK]
        v3 = (paramA * v1 + paramC * v2) % paramM
        serie.append(v3)
        v1 = v3

    # Se recorta la serie según el parámetro K
    serieResultado = serie[paramK:]
    return serieResultado