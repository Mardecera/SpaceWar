"""
+---------------------------------------+
|Creado por: Jonathan Cervantes Alarcon |
+---------------------------------------+
"""

import pygame, sys
import os
from pygame.locals import *
from cuadrado import *
from proyectil import *
from enemigos import *

ancho = 720
alto = 480

def main():

    pygame.display.set_icon(pygame.image.load("img/icono.png"))
    
    colorVen = pygame.Color(10, 23, 50) #colores rgb
    fondo = pygame.image.load("img/fondo_borroso.png")
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Space War")

    #reloj = pygame.time.Clock()

    player = Cuadrado(ancho, alto, 50)
    enemigo = Enemigo(50)
    vida = True
    
    while True:

        #reloj.tick(560) #para regular los frames
        #ventana.fill(colorVen) #fill, funcion para dar color a la ventana
        ventana.blit(fondo, (0, 0))        
        
        for evento in pygame.event.get(): #capta el evento en ese momento de la ventana
            if evento.type == pygame.QUIT: #si es tipo del evento es quit, osea se hace click en el boton close
                pygame.quit() #se cierran los modulos de pygame
                sys.exit() #se sale del sistema(ventana)
            if vida == True:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == K_SPACE:
                        player.disparar(player.posx + (player.tamanio/2) - (11), player.posy) #aqui se modifica l dbujo de la bala
                        
        if vida == True:
            
            pulsada = pygame.key.get_pressed()
            """---------------------------------"""
            if pulsada[K_a]:
                player.posx -= player.velocidad
                if player.posx < 0:
                    player.posx = 0
            """---------------------------------"""
            if pulsada[K_d]:
                player.posx += player.velocidad
                if player.posx > (ancho - player.tamanio):
                    player.posx = (ancho - player.tamanio)
                
        """Este if dibuja la bala que se obtuvo en el primer for y la dibuja"""
        if len(player.listDisparo) == 1:
            for bala in player.listDisparo:
                bala.dibujar(ventana)
                bala.trayectoria()

                if bala.topy < 0:
                    player.listDisparo.remove(bala)
                
        player.dibujar(ventana)
        enemigo.dibujar(ventana)
        pygame.display.update() #caso contrario toda la ventana se actualiza por cada iteracion

if __name__ == '__main__':
    
    os.environ["SDL_VIDEO_CENTERED"] = "1" #Para centrar pantalla, antes del pygame.init e importando os
    pygame.init() #inicia todos los modulos
    main() #llama a la funcion que contiene la ventana 
