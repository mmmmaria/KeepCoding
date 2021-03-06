import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__ (self):
        self.custome = pygame.image.load("images/termo1.png")
    
    def convertir(self, grados, toUnidad):
        resultado =0
        if toUnidad == "F":
            resultado = grados *9/5 +32
        elif toUnidad == "C":
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
            
        return "{:10.2f}".format(resultado)
#         return int(resultado) Si pusiera esto saldría ok pero sin decimales, i.e., sin precisión
    
class Selector():
    __tipoUnidad = None
    
    def __init__(self, unidad = "C"):
        self.__customes =[]
        self.__customes.append(pygame.image.load("images/posiF.png"))
        self.__customes.append(pygame.image.load("images/posiC.png"))
        
        self.__tipoUnidad = unidad
    
    def custome(self): #es un getter para el Selector
        if self.__tipoUnidad == "F":
            return self.__customes[0]
        else:
            return self.__customes[1]
    
    def change (self):
        if self.__tipoUnidad == "F":
            self.__tipoUnidad = "C"
        else:
            self.__tipoUnidad = "F"
            
    def unidad(self): #los getter solo necesitan el parametro self
        return self.__tipoUnidad
        
class NumberInput(): #entrada del valor numérico
    __value = 0 #declaro los atributos
    __strValue = ""
    __position = [0,0]
    __size = [0,0]
    __pointsCount = 0
    
    def __init__ (self, value = ""): #pongo el constructor; teniamos value=0 pero lo hemos cambiado a value=""para inicializarlo en pantalla sin nada
        self.__font = pygame.font.SysFont("Arial", 24)
        self.value(value) #es la función de abajo
        
    def on_event(self,event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue) < 10 or (event.unicode == '.' and self.__pointsCount == 0): #o if event.unicode in '0123456789':
                #<10 para que quepa en la máquina
                self.__strValue += event.unicode #el += acumula los números sin límite 
                self.value(self.__strValue)
                if event.unicode == '.': #para que solo haya un punto
                    self.__pointsCount +=1
                    
            elif event.key == K_BACKSPACE:#por si me he equivocado al meter el número, es la tecla"suprimir"
                if self.__strValue[-1] == '.':
                    self.__pointsCount -= 1
                self.__strValue = self.__strValue[:-1]#borro el último número
                self.value(self.__strValue)
                                
    def render(self): #2 rectángulos: textBlock es el de texto (cadena renderizada), rect es el blanco
        textBlock = self.__font.render(self.__strValue, True, (74,74,74)) #True que se expanda a todo el cuadrado, (,,,) color RGB
        rect = textBlock.get_rect() #rect es el rectángulo de texto, el pequeño, lo crea pequeño y en la posición (0,0), luego lo cambio
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size #lo hemos renderizado
        
#         return {
#             "fondo":rect,
#             "texto":textBlock
#                 }
    
        return (rect,textBlock)
    
#         para informar, como los atributos (value, strValue, position,size) son privados, tyenemos que usar getter y setters
    def value(self, val=None): #si el valor es erroneo, pasa, no hace nada, no da error. Controla las dos propiedades: value,srtValue
        if val == None:
            return self.__value
        else:
            val = str(val) #queremos el numero como cadena porque así lo exige el display
            try:
                self.__value = float(val)
                self.__strValue = val
                if '.' in self.__strValue:
                    self.__pointsCount = 1
                else:
                    self.__pointsCount = 0
            except:
                pass
           
    def width(self, val= None):
        if val ==None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = float(val)
            except:
                pass
       
    def height(self, val= None):
        if val ==None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                pass
                
    def size(self, val= None):
        if val == None:
            return self.__size
        else:
            try:
                w=int(val[0])
                h=int(val[1])
                self.__size = [int(val[0]), int(val[1])]
            except:
                pass
            
    def posX(self,val=None):
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass
            
    def posY(self,val=None):
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass
            
    def pos(self,val=None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]),int(val[1])]
            except:
                pass
            
class MainApp(): 
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self): #este es el constructor
        self.__screen = pygame.display.set_mode((290,415))
        pygame.display.set_caption("Termómetro")
        self.__screen.fill((244,236,203)) #color amarillento, la pongo aquí y tendré que ponerla abajo en el renderizado para repetirla cada vez
        
        self.termometro = Termometro()
        self.entrada = NumberInput()
        self.entrada.pos((106,58))#coordenadas del rectangulo de texto
        self.entrada.size((133,28))
       
        self.selector = Selector() #lo tengo que crear aquí
        
    def __on_close(self):
        pygame.quit()
        sys.exit()        

    def start(self): #control de eventos y renderizado
        while True:
            for event in pygame.event.get(): #capturo los eventos
                if event.type ==QUIT:
                    self.__on_close()
                    
                self.entrada.on_event(event) #delega la comprobación de eventos a la función on_event
                
                if event.type == pygame.MOUSEBUTTONDOWN: #MOUSEBUTTONDOWN es hacer un click con el ratón
                    self.selector.change()
                    grados = self.entrada.value() #getter
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir(grados, nuevaUnidad)
                    print(temperatura) 
                    #self.entrada.value(int(temperatura)) #funcionaría también
                    self.entrada.value(temperatura) 
                                       
            #Pintamos el fondeo de pantalla (cada vez)
            self.__screen.fill((244,236,203))
            #Pintamos el termometro en su posición        
            self.__screen.blit(self.termometro.custome, (50,34)) #pintamos el termometro (cada vez)
            #Pintamos el cuadro de texto
            text = self.entrada.render()#obtenemos rectángulo balnco y foto del texto y lo asignamos a la variable text
            pygame.draw.rect(self.__screen, (255,255,255), text[0]) #creamos el rectángulo balnco en su posición con sus datos(pos y size), el 255 es el color balnco
            self.__screen.blit(text[1],self.entrada.pos())#pintamos la foto del texto (text[1]) en la misma posición
            #pintamos el selector (su disfraz)
            self.__screen.blit(self.selector.custome(), (112,153))
            
            #la función render devuelve dos valores: rect,TextBlock y a mi me interesa textBlock, por eso text[1]    
            pygame.display.flip()
            
if __name__ == '__main__':
    pygame.init()
    app = MainApp() #creo la instancia
    app.start() #me meto en el bucle principal de la instancia, la ejecuto