import pygame, sys

width = 640
height = 480

#pintamos la pantalla de inicio
screen = pygame.display.set_mode ((width, height))
screen.fill((246,147,48)) #pongo el fondo naranja
pygame.display.set_caption("Ciclo básic de pygame")

pygame.init() #inicializamos pygame y comienza a atender eventos
#pygame.font.init()

gameOver = False
while not gameOver:
    for event in pygame.event.get(): #el buffer de eventos de pygame (que es pygame.event.get()) nos da una lista de los eventos que se prodcen
        if event.type == pygame.QUIT:
            gameOver = true
    pygame.display.flip() #refresco la imagen
    
pygame.quit()
sys.exit() #nos asegura que se cierra el juego y python