# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:31:35 2015

@author: Thomas Rodriguez et Maxime Thibert
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
    
def tuyaux(tuyau,x_tuyau,y_tuyau):
    surface.blit(tuyau,(x_tuyau,y_tuyau))
   


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


def defilement():
    pygame.init()
 
    ecran = pygame.display.set_mode((1280, 720))

    pygame.display.set_caption("")
 
    clock = pygame.time.Clock()
 
    background1 = pygame.image.load('fondflappy.png')
    background2 = pygame.image.load('fondflappy.png')
     
    abscisse_background1 = 0
    abscisse_background2 = background1.get_left()
 
    while True:
 
        ecran.blit(background1, (0, abscisse_background1))
        ecran.blit(background2, (0,abscisse_background2))
 
        pygame.display.update()
 
        abscisse_background1 -= 1
        abscisse_background2 -= 1
    
        if abscisse_background1 == -1 * background1.get_left():
            abscisse_background1 =abscisse_background2 + background2.get_left()
        if background2 == -1 * background2.get_left():
            abscisse_fond2 = abscisse_background1 + background1.get_left()
 
    clock.tick(60)


def main(): 
    fond = pygame.image.load("fondflappy.png")
    oiseau = pygame.image.load("flappy2.png")
    tuyau = pygame.image.load("tuyau.png")
    x = 150
    y = 200
    y_mouv = 0
    x_tuyau = surfaceL
    y_tuyau = random.randint(-380,-200)
    tuyau_vitesse = 2
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
            y_tuyau = random.randint(-380,-200)
        surface.blit(fond,(0,0))         
        flappy(x,y, oiseau)
        tuyaux(tuyau,x_tuyau,y_tuyau)
        x_tuyau -= tuyau_vitesse # bouge de 6 pixels
        #defilement()
        pygame.display.update() #rafraichissement
        
        
        
main()
pygame.quit()
quit()
