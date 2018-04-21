# -*- coding: utf-8 -*-
# Métodos de testeo para series de números (pseudo)aleatorios

def testChiCuadrado(serieNumeros,cantDigitos):
    frecuenciaObservada = range(cantidadDigitos)
    for num in serieNumeros:
        frecuenciaObservada[num] += 1
    frecuenciaTeorica = len(serieNumeros) / cantidadDigitos
    gradosLibertad = cantDigitos - 1
    for valor in frecuenciaObservada:
        numerador = (frecuenciaObservada - frecuenciaTeorica) ** 2
