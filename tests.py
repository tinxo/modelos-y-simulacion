# -*- coding: utf-8 -*-
#Test de Chi-Cuadrada

# Constantes para no cargar la tabla completa (por ahora)
valoresGL9 = {
    0.01 : 12.43,
    0.05 : 11.32
    }

valoresGL2 = {
    0.01 : 0.0,
    0.05 : 0.0
    }

def testChiCuadrado(serieNumeros,cantidadDigitos,margenError):
    print(serieNumeros)
    frecuenciaObservada = [0] * cantidadDigitos
    
    for num in serieNumeros:
        frecuenciaObservada[num] += 1
    
    frecuenciaTeorica = len(serieNumeros) / cantidadDigitos
    gradosLibertad = cantidadDigitos - 1
    chi = 0
    for valor in frecuenciaObservada:
        numerador = (valor - frecuenciaTeorica) ** 2
        chi += (numerador / frecuenciaTeorica)
    
    if (gradosLibertad == 9):
        # Chi cuadrado tradicional
        if valoresGL9[margenError] >= chi:
            return True
    elif (gradosLibertad == 2):
        # Monobits
        if valoresGL2[margenError] >= chi:
            return True
    else:
        return False

def testPoker(serieNumeros):
    return True

def testRachas(serieNumeros):
    return True

def testRachasLargas(serieNumeros):
    return True
