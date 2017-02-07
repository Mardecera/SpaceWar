import pygame, sys
from pygame.locals import *
from proyectil import * #importo todas las clases del archivo proyectil
haya
class Cuadrado(pygame.sprite.Sprite):
    def __init__(self, posx, posy, tamanio):
        pygame.sprite.Sprite.__init__(self)
        
        self.vida = True #vida del jugador
        #self.color = pygame.Color(120, 110, 120)
        self.posx = (posx/2) - (tamanio / 2) #posicion horizontal del jugador
        self.posy = (posy - (tamanio +(tamanio / 2))) #posicion vertical del jugador
        self.velocidad = 0.3
        self.tamanio = tamanio #tamaño del cuadrado
        self.listDisparo = [] #lista para añadir los disparos


    def disparar(self, x, y): #clase que ubica e inserta la bala en la lista
        bala = Proyectil(x, y)
        self.listDisparo.append(bala)
    
    def dibujar(self, ventana):
        imagen = pygame.image.load("img/yo.png")
        imagen = pygame.transform.scale(imagen,
            (self.tamanio, self.tamanio))
        ventana.blit(imagen, (self.posx, self.posy))
        #dibuja el cuadrado en la pantalla dada
        """pygame.draw.rect(ventana, self.color,
            (self.posx, self.posy, self.tamanio,
                self.tamanio))"""

