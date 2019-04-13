v1 = 23
v2 = 67
ctrl = 77

n = 10

serie = []
serie.append(v1)
serie.append(v2)

while (len(serie) <= n):
    if ((v1 + v2) <= ctrl):
        v3 = v2 + v1 #k = 0
    else:
        v3 = v2 + v1 + ((-1) * ctrl)
    serie.append(v3)
    v1 = v2
    v2 = v3

print(serie)

    