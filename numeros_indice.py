def validarProbabilidades(vectorProbabilidades):
    suma = 0
    for valor in vectorProbabilidades:
        suma += valor
    if (suma == 1):
        return True
    else:
        return False

def crearMatrizNumerosIndice(cantClases):
    matriz = []
    for fila in range(2):
        # 2 filas > valor inferior y valor superior
        unaFila = []
        for columna in range(cantClases):
            unaFila.append(0)
        matriz.append(unaFila)
    return matriz

print("Ingrese la cantidad de marcas de clase:")
cantidadClases = input()
contador = 0
probabilidadClase = []
probabilidadAcumulada = []
while contador < cantidadClases:
    print("Ingrese el valor de la probabilidad (0 < px < 1) de la marca de clase nro. " + str(contador + 1) + ":")
    px = input()
    probabilidadClase.append(px)
    if contador == 0:
        probabilidadAcumulada.append(probabilidadClase[contador])
    else:
        probabilidadAcumulada.append(probabilidadClase[contador] + probabilidadClase[contador - 1])
    contador += 1

numerosIndices = crearMatrizNumerosIndice(cantidadClases)

# opción 1 - probabilidades
numerosIndices[1][0] = 
contador = 1



# opción 2 - valores

