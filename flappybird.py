# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:31:35 2015

@author: Thomas Rodriguez et Maxime Thibert

Demander pour les nombreux if (elif ?) et nombreuses variables ds fonction main
"""
import pygame
import time
import random

pygame.init()
surfaceL = 800
surfaceH = 500
surface = pygame.display.set_mode((surfaceL,surfaceH))
pygame.display.set_caption("Flappy Bird")
horloge = pygame.time.Clock()



def flappy(x,y,oiseau):
    
    surface.blit(oiseau,(x,y))
    
def tuyaux(tuyau,tuyau_bas,x_tuyau,y_tuyau,ecart): 
    surface.blit(tuyau,(x_tuyau,y_tuyau))
    surface.blit (tuyau_bas,(x_tuyau,y_tuyau+509+ecart)) #509 = taille tuyau

def bord_defile(bord,x_bord,y_bord):
    surface.blit(bord,(x_bord,y_bord))



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
import pygame, sys
import pygame.locals


def Score(score,x_tuyau):
    black = (0, 0, 0)    
    font = pygame.font.Font(None ,50)
    textesurface = font.render(("Score: "+str(score)), True, black)
    surface.blit(textesurface, [0, 0])

    
def collision(xf,yf,xt,yt,ecart):
    if xf > xt-135 and xf < xt+75 and (yf >= yt+509 or yf <= yt+509+ecart):
        message("Game over",surfaceL,surfaceH)
    
    

def main(): 
    fond = pygame.image.load("fondflappy.png")
    oiseau = pygame.image.load("flappy2.png")
    tuyau = pygame.image.load("tuyau.png")
    bord = pygame.image.load("bord.png")
    tuyau_bas =  pygame.transform.rotate(tuyau, 180)
    x_flappy = 68
    y_flappy = 50
    x = 150
    y = 200
    y_mouv = 0
    x_tuyau = surfaceL
    y_tuyau = random.randint(-400,-280)
    ecart = 3*y_flappy
    tuyau_vitesse = 2
    score = 0
    x_bord = 16
    y_bord = 470
    game_over = False
    while (game_over == False) :  #quitter boucle inf
        for event in pygame.event.get(): #recherche parmi evenements
            if event.type == pygame.QUIT:
                game_over = True 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    y_mouv = -5
            if event.type == pygame.KEYUP:
                y_mouv = 2
        y += y_mouv
        if y>surfaceH-5 or y <-5: #2 bords en hauteur
            message("Game over",surfaceL,surfaceH)
        
        if x_tuyau < (0):
            x_tuyau =  surfaceL
            y_tuyau = random.randint(-400,-280)
            score +=1
            if score >= 2:
                ecart = 2*y_flappy
                tuyau_vitesse = score
                if score >= 10:
                    tuyau_vitesse = 10
                
        surface.blit(fond,(0,0))         
        flappy(x,y, oiseau)
        tuyaux(tuyau,tuyau_bas,x_tuyau,y_tuyau, ecart)
        x_tuyau -= tuyau_vitesse # bouge de 6 pixels
        Score(score,x_tuyau)
        #collision(x_flappy,y_flappy,x_tuyau,y_tuyau,ecart)
        if x_bord < -339 :
            x_bord = 16
        bord_defile(bord,x_bord,y_bord)
        x_bord -= tuyau_vitesse
        pygame.display.update() #rafraichissement
        
        
        
main()
pygame.quit()
quit()
