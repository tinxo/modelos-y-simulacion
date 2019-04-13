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

def convertirRango(serie, limiteInferior, limiteSuperior):
    res = []
    for num in serie:
        

#prueba para digitos
numeros = [1234, 5678, 0, 231]
n2 = obtenerDigitos(numeros)
print(n2)

#prueba para binarios
n3 = convertirBinario(n2)
print(n3)