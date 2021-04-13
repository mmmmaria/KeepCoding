from functools import reduce

def doble(x):
    return x+x

lista = [1,3,-1, 15, 9]

listaDobles = map(lambda x: x*2, lista)
listaDobles1 = map(doble, lista)
# print(list(listaDobles1))
# print(list(listaDobles))

def esPar(x):
    return x % 2 == 0

listaPares = filter (lambda x: x % 2 ==0, lista)
listaPares1 = filter (esPar, lista) #las funciones que usamos con filter tienen qu dar True o False
print(list(listaPares))
print(list(listaPares1))

sumatorio = reduce(lambda x,y : x + y, lista) 
print(sumatorio) #x representa el valor acumulado, que es el que me va a devolver el reduce
sumatorioDobles = reduce(lambda x,y: x+y*2, lista) #1+6-2+30+18, el primero no hace el doble
print(sumatorioDobles)

suma100 = reduce (lambda x,y: x+y, range(101)) # en lugar de la lista le meto el range
print(suma100)