import turtle

class Circuito():
    corredores = []
    __posStartY = (-30,-10,10,30) #privado y tupla, para que sea inmutable, posiciones de inicio Y centradas
    __colorTurtle = ('red','blue','green','orange')
    
    def __init__(self, width, height):
#       self.width = width #podríamos ponerlo privado #Dice Mon qe no hacen falta porque los pongo a capón
#       self.height = height
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__starline = -width/2 + 20 #empezamos 20m mas allá del límite de la pantalla
        self.__finishline = width/2 - 20
        
        self.__createRunners()
        
    def __createRunners(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i]) #color de cada tortuga
            new_turtle.shape('turtle')
            new_turtle.penup() #para que no salgan las lineas desde donde se crean hasta su posición
            new_turtle.setpos(self.__starline, self.__posStartY[i])
            
            self.corredores.append(new_turtle)
            
       
        
        
if __name__ == '__main__': #por si lo usamos como módulo en otros programas
    circuito = Circuito(640,480)