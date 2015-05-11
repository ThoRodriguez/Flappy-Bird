# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:08:38 2015

@author: Thomas
"""

import pygame
import time

pygame.init()
surfaceL = 800
surfaceH = 500
surface = pygame.display.set_mode((surfaceL,surfaceH))
pygame.display.set_caption("Flappy Bird")
horloge = pygame.time.Clock()



def flappy(x,y,oiseau):
    
    surface.blit(oiseau,(x,y))
    



def message(texte,surfaceL,surfaceH):
    gameover = pygame.font.Font("04b.ttf",140)
    gameoversurface, gameoverRect = creaTexte(texte, gameover) #contient 1 
                                                           #texte et 1 police
    gameoverRect.center = surfaceL/2, (surfaceH/2)-50
    surface.blit(gameoversurface, gameoverRect)
    
    pygame.display.update()
    time.sleep(2)
    while rejoueOUquitte() == None:   #tant que RoQ renvoie a rien
        horloge.tick()              #bloque tout
    main()
    
    
def creaTexte(texte, police):
    white = (255,255,255)
    textesurface = police.render(texte, True, white)
    return textesurface, textesurface.get_rect()


def rejoueOUquitte():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYUP:
            continue
        return event.key
    return None



def main(): 
    fond = pygame.image.load("fondflappy.png")
    oiseau = pygame.image.load("flappy2.png")
    x = 150
    y = 200
    y_mouv = 0
    game_over = False
    while (game_over == False) :  #quitter boucle inf
        for event in pygame.event.get(): #recherche parmi evenements
            if event.type == pygame.QUIT:
                game_over = True 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    y_mouv = -10
            if event.type == pygame.KEYUP:
                y_mouv = 3
        y += y_mouv
        if y>surfaceH-5 or y <-5: #2 bords en hauteur
            message("Game over",surfaceL,surfaceH)
        surface.blit(fond,(0,0))         
        flappy(x,y, oiseau)
        pygame.display.update() #rafraichissement
        
        
        
main()
pygame.quit()
quit()