import pygame, sys
from pygame.locals import *

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)

        self.color = pygame.Color(120, 110, 120)
        self.velocidad = 0.3
        self.topy = posy #posicion vertical de la bala
        self.topx = posx #posicion horizontal de la bala
        self.tamanio = 10 #tamaño de la bala

    def trayectoria(self):
        self.topy -= self.velocidad #la posicion de la bala va reduciendo dando el efecto de movimiento
    
    def dibujar(self, ventana):
        imagen = pygame.image.load("img/mi_bala.png")
        imagen = pygame.transform.scale(imagen,
            (self.tamanio*2, self.tamanio*2))
        ventana.blit(imagen, (self.topx, self.topy))
        """pygame.draw.rect(ventana, self.color,
            (self.topx, self.topy, self.tamanio,
                self.tamanio)) #dibuja la bala en la pantalla"""
