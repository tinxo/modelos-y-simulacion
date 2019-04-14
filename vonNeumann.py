import funciones as fn
# Von Neumann
def generadorVonNeumann(valorSemilla,cantidadGenerar):
    serie = [valorSemilla]
    while len(serie) < cantidadGenerar:
        cuadrado = valorSemilla ** 2
        ochoCifras = str(cuadrado)
        while (len(ochoCifras) < 8):
            #se debe completar con ceros a la izquierda
            ochoCifras = "0" + ochoCifras
        valorSemilla = int(ochoCifras[2:-2])
        if not(fn.verificarDobleCero(valorSemilla)):
            #se suma un valor X al número para poder continuar con la generación
            valorSemilla += 37
        serie.append(valorSemilla)
    return serie
