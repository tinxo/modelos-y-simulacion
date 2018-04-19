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
print("Arrancamos. Ingrese un número de 4 digitos como -semilla-\n")
semilla = input()
print("Ingrese la cantidad de números a generar")
cantidad = input()
numerosGenerados = [semilla]
while cantidad > 0:
    cuadrado = semilla ** 2
    ochoCifras = str(cuadrado)
    while (len(ochoCifras) < 8):
        #se debe completar con ceros a la izquierda
        ochoCifras = "0" + ochoCifras
    semilla = int(ochoCifras[2:-2])
    numerosGenerados.append(semilla)
    if not(verificarDobleCero(semilla)):
        #se suma un valor X al número para poder continuar con la generación
        semilla += 37
    cantidad -= 1
print("Proceso de generación finalizado. Resultados:\n")
print(numerosGenerados)
