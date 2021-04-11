def maxi(*l):
    if len(l) == 0:
        return 0
    m = l[0] #m es el maximo, si solo hay un valor el maximo es ese valor
    for ix in range(1,len(l)): #el elemento o ya lo he comprobado, empiezo en 1
        if l[ix] > m:
            m = l[ix]
    return m

def mini(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range(1,len(l)):
        if l[ix] < m:
            m = l[ix]
    return m

def media(*l):
    if len(l) == 0:
        return 0
    suma=0
    for valor in l:
        suma += valor
    return suma/len(l)

funciones = {
    'max':maxi,
    'min':mini,
    'med':media
    }

def returnF(nombre): #esta funcion me va a devolver otra funcion
    nombre=nombre.lower()
    if nombre.lower() in funciones.keys():
        return funciones[nombre]
    return None