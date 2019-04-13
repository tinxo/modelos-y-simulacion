#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("Congruencias: Relac. Fundamental")

v1 = 14
v2 = 17
paramA = 3243
#paramC = 0
#paramK = 16
paramM = 1000

serie = []
n = 100


while (len(serie) <= n):
    v3 = (paramA * v1) % paramM
    serie.append(v3)
    v1 = v3
    #break

print(serieResultado)