# -*- coding: utf-8 -*-
#Generador de números aleatorios


#Métodos generales o auxiliares
def verificarDobleCero(num):
    numStr = str(num)
    if (numStr[len(numStr) -1] == "0" and numStr[len(numStr) -2] == "0"):
        #error
        return False
    else:
        return True

def extraerUnidades(serieNumeros):
    nuevaSerie = []
    idx = 0
    while idx < len(serieNumeros):
        valor = str(serieNumeros[idx])
        for n in range(len(valor)):
            nuevaSerie.append(int(valor[n]))
        idx += 1
    return nuevaSerie

#Von Neumann
def metodoVonNeumann():
    print("Inicio del generador. Ingrese un número de 4 digitos como -semilla-:")
    semilla = input()
    print("Ingrese la cantidad de números a generar:")
    cantidad = input()
    res = generadorVonNeumann(semilla,cantidad)
    print("Proceso de generación mediante el método de Von Neumann finalizado. Resultados:\n")
    print(res)
    print
    print("Resultados transformados a una serie de unidades:\n")
    resUnidades = extraerUnidades(res)
    print(resUnidades)
    print

def generadorVonNeumann(valorSemilla,cantidadGenerar):
    numerosGenerados = [valorSemilla]
    while cantidadGenerar > 0:
        cuadrado = valorSemilla ** 2
        ochoCifras = str(cuadrado)
        while (len(ochoCifras) < 8):
            #se debe completar con ceros a la izquierda
            ochoCifras = "0" + ochoCifras
        valorSemilla = int(ochoCifras[2:-2])
        numerosGenerados.append(valorSemilla)
        if not(verificarDobleCero(valorSemilla)):
            #se suma un valor X al número para poder continuar con la generación
            valorSemilla += 37
        cantidadGenerar -= 1
    return numerosGenerados

#Fibonacci
def metodoFibonacci():
    print("Inicio del generador. Ingrese un número de 4 digitos como -valor 1-:")
    val1 = input()
    print("Ingrese un número de 4 digitos como -valor 1-:")
    val2 = input()
    print("Ingrese un número de 4 digitos como -valor A-:")
    valA = input()
    print("Ingrese la cantidad de números a generar:")
    cantidad = input()
    res = generadorFibonacci(val1,val2,valA,cantidad)
    print("Proceso de generación mediante el método de Von Neumann finalizado. Resultados:\n")
    print(res)
    print
    print("Resultados transformados a una serie de unidades:\n")
    resUnidades = extraerUnidades(res)
    print(resUnidades)
    print

def generadorFibonacci(valor1,valor2,valorA,cantidadGenerar):
    numerosGenerados = [valor1,valor2]
    n = 1
    while n < cantidadGenerar:
        if (numerosGenerados[n] + numerosGenerados[n - 1]) > valorA:
            k = 0
        else:
            k = -1
        valor3 = numerosGenerados[n] + numerosGenerados[n - 1] + k * valorA
        numerosGenerados.append(abs(valor3))
        n += 1
    return numerosGenerados



#main
print("Inicio del generador. Seleccione el método a utilizar:")
print("-1- Von Neumann.")
print("-2- Fibonacci.")
print("-3- Salir.")
opcion = input()
if (opcion == 1):
    metodoVonNeumann()
elif (opcion == 2):
    metodoFibonacci()
print "Fin de la ejecución."





