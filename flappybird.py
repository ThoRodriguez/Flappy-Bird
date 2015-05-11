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



def flappy(x,y,oiseau):
    
    surface.blit(oiseau,(x,y))
    

def GO():
    message("Game Over")

def message(texte):
    gameover = pygame.font.Font("04b.ttf",140)
    rejouer = pygame.font.Font("04b.ttf",30)
    gameoversurface, gameoverRect = creaTexte(texte, gameover) #contient 1 texte et 1 police
    gameoverRect.center = surfaceL/2, (surfaceH/2)-50
    surface.blit(gameoversurface, gameoverRect)
    
    rejouersurface, rejouerRect = creaTexte("Rejouer ?", rejouer)
    rejouerRect.center = surfaceL/2, (surfaceH/2)+50
    surface.blit(rejouersurface, rejouerRect)
    
    pygame.display.update()
    
    
def creaTexte(texte, police):
    white = (255,255,255)
    textesurface = police.render(texte, True, white)
    return textesurface, textesurface.get_rect()


def main(): 
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
            GO()
            pygame.quit()
        surface.blit(fond,(0,0))         
        flappy(x,y, oiseau)
        pygame.display.update() #rafraichissement
            
    
        
main()
pygame.quit()
quit()