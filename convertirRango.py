# Número generado desde el método 
numero_original = 0.99

# Rango de valores del escenario en el que se quiere ajustar
rango = [-2, 35]

# Primera adaptación: número original ajustado entre [0, 1]
# original_adaptado = numero_original / 10000

# Aplicación de la fórmula
cantidad_simbolos = rango[1] - rango[0]
numero_nuevo = rango[0] + abs(numero_original * cantidad_simbolos)

# Vista del resultado
print(f'Valor original: {numero_original} - Valor ajustado: {numero_nuevo}')

