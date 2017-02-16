import pygame, sys
from pygame.locals import *
from proyectil import * #importo todas las clases del archivo proyectil

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, tamanio):
        pygame.sprite.Sprite.__init__(self)
        
        self.vida = True
        self.posx = 1 #posicion horizontal del jugador
        self.posy = 1 #posicion vertical del jugador
        self.velocidad = 0.3
        self.tamanio = tamanio #tamaño del cuadrado
        self.listDisparo = [] #lista para añadir los disparos


    def disparar(self, x, y): #clase que ubica e inserta la bala en la lista
        bala = Proyectil(x, y)
        if len(self.listDisparo) == 0: #para que dispare una bala por vez
            self.listDisparo.append(bala)
    
    def dibujar(self, ventana):
        imagen = pygame.image.load("img/first_row.png")
        imagen = pygame.transform.scale(imagen,
            (self.tamanio, self.tamanio))
        ventana.blit(imagen, (self.posx, self.posy))
        