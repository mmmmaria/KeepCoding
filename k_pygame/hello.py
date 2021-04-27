import pygame as pg
pantalla = pg.display.set_mode ((600,400)) #podría haber muchos más parámetros que el tamaño: bordes, etc
pg.display.set_caption ("Hola")

pg.init()

game_over = False

while not game_over:
    #Gestión de eventos
    for evento in pg.event.get(): #en cada ciclo vacia la lista de eventos con esta instrucción
        pass 

    #Gestión del estado
    print("Hola mundo")

    #Refrescar pantalla
    pantalla.fill((0,255,0)) #en la memoria de tu programa
    pg.display.flip() #en la memoria grafica