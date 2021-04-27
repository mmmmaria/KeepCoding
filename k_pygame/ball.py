import pygame as pg
import sys

ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
ANCHO = 800
ALTO = 600

pg.init()
pantalla = pg.display.set_mode((ANCHO,ALTO))

game_over = False
x=ANCHO//2
y=ALTO//2
vx=-5
vy=-5
reloj = pg.time.Clock() #para ralentizar el movimiento de la bola

while not game_over:
    reloj.tick(60)
    #Gestión de eventos
    for evento in pg.event.get():
        if evento.type ==pg.QUIT:
            game_over = True

    #Modificación de estado
    x += vx
    y += vy

    if y<=0 or y >= ALTO:
        vy = -vy #vy*=-1 ó vy=-vy es cambiar el signo
    
    if x<=0 or x >= ANCHO:
        vx = -vx
    
    #Gestión de la pantalla
    pantalla.fill(NEGRO)
    pg.draw.circle(pantalla, ROJO, (x,y),10)

    pg.display.flip()

pg.quit()
sys.exit()


