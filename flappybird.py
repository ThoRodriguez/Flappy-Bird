# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:08:38 2015

@author: Thomas
"""

import pygame
pygame.init()

surfaceL = 800
surfaceH = 500
oiseauL = 50
oiseauH = 66
surface = pygame.display.set_mode((surfaceL,surfaceH))
pygame.display.set_caption("Flappy Bird")
fond = pygame.image.load("fondflappy.png")
oiseau = pygame.image.load("flappy2.png")

def flappy(oiseau):
    surface.blit(oiseau,(150,200))

    
def main():    
    game_over = False
    while (game_over == False) :  #quitter boucle inf
        for event in pygame.event.get(): #recherche parmi evenements
            if event.type == pygame.QUIT:
                game_over = True 
           
    surface.blit(fond,(0,0))         
    flappy(oiseau)
    pygame.display.update()

main()
pygame.quit()
quit()