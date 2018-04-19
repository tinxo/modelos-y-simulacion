# -*- coding: utf-8 -*-
#Generador de números aleatorios

def verificarDobleCero(num):
    numStr = str(num)
    if (numStr[len(numStr) -1] == "0" and numStr[len(numStr) -2] == "0"):
        #error
        return False
    else:
        return True

#Von Neumann
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
def generadorFibonacci(valor1,valo2,valorA):
    return 0

def metodoVonNeumann():
    print("Inicio del generador. Ingrese un número de 4 digitos como -semilla-:")
    semilla = input()
    print("Ingrese la cantidad de números a generar:")
    cantidad = input()
    res = generadorVonNeumann(semilla,cantidad)
    print("Proceso de generación mediante el método de Von Neumann finalizado. Resultados:\n")
    print(res)
    print


#main
print("Inicio del generador. Seleccione el método a utilizar:")
print("-1- Von Neumann.")
print("-2- Fibonacci.")
print("-3- Salir.")
opcion = input()
if (opcion == "1"):
    metodoVonNeumann
    print "hola"
elif (opcion == "2"):
    metodoFibonacci
print "Fin de la ejecución."





