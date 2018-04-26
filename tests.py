# -*- coding: utf-8 -*-
# Métodos de testeo para series de números (pseudo)aleatorios

valoresGL9 = {
    0.01 : 12.43,
    0.05 : 11.32
    }

def testChiCuadrado(serieNumeros,cantDigitos,margenError):
    frecuenciaObservada = [0] * cantDigitos
    for num in serieNumeros:
        frecuenciaObservada[num] += 1
    frecuenciaTeorica = len(serieNumeros) / cantidadDigitos
    gradosLibertad = cantDigitos - 1
    chi = 0
    for valor in frecuenciaObservada:
        numerador = (frecuenciaObservada - frecuenciaTeorica) ** 2
        chi += (numerador / frecuenciaTeorica)
    if (gradosLibertad == 9):
        # Chi cuadrado tradicional
        if valoresGL9[margenError] <= chi
            return True
    elif (gradosLibertad == 2):
        # Monobits
        if valoresGL2[margenError] <= chi
            return True
    else:
        return False

def testPoker(serieNumeros):
    return True

def testRachas(serieNumeros):
    return True

def testRachasLargas(serieNumeros):
    return True
