from functools import reduce

def sumatorioClasico(l):
    resultado = 0   #con reduce este paso previo no lo tengo y por esoes peor, al primer elemento no le aplica
    for valor in l:
        resultado += valor
    return resultado

def sumatorioDobleClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor * 2
    return resultado

def productoTotal(l):
    resultado = 1
    for valor in l:
        resultado += valor
    return resultado

lista = [1, 3, -1, 15, 9]

sumatorio = reduce (lambda x,y : x + y, lista)

l = lista [:] #esto hace una copia de la lista entera
l.insert(0,0) #añado el elemento neutro para la suma = 0 en la posición 0, así solvento el tema de reduce que no aplica la 1er elemento
sumatorioDobles = reduce (lambda x,y : x+y*2, l)

print(sumatorio)
print(sumatorioDobles)