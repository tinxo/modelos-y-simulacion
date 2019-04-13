#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("Congruencias: Relac. Fundamental")

v1 = 14
v2 = 17
paramA = 3243
paramC = 23
paramK = 16
paramM = 1000

serie = []
n = 100

for x in range(paramK):
    v3 = (paramA * v1 + paramC * v2) % paramM
    serie.append(v3)
    v1 = v3
    

print(serie)

while (len(serie) <= n + paramK):
    v2 = serie[len(serie) - paramK]
    print(v2)
    v3 = (paramA * v1 + paramC * v2) % paramM
    serie.append(v3)
    v1 = v3
    #break

serieResultado = serie[paramK:]
print(serieResultado)