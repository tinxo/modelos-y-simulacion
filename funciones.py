#Funciones complementarias

def verificarDobleCero(num):
    numStr = str(num)
    if (numStr[len(numStr) -1] == "0" and numStr[len(numStr) -2] == "0"):
        #error
        return False
    else:
        return True

def obtenerDigitos(serie):
    res = []
    for num in serie:
        num = str(num)
        for digito in num:
            res.append(int(digito))
    return res

def convertirBinario(serie):
    res = []
    for num in serie:
        if (num <= 4):
            res.append(0)
        else:
            res.append(1)
    return res

#TODO: convertir valores individuales a un rango específico

#prueba para digitos
numeros = [1234, 5678, 0, 231]
n2 = obtenerDigitos(numeros)
print(n2)

#prueba para binarios
n3 = convertirBinario(n2)
print(n3)