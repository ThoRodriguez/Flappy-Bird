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



def flappy(x,y,oiseau, rotate):

    oiseau = pygame.transform.rotate(oiseau, rotate)
    surface.blit(oiseau,(x,y))


def tuyaux(tuyau,tuyau_bas,x_tuyau,y_tuyau,ecart): 
    surface.blit(tuyau,(x_tuyau,y_tuyau))
    surface.blit (tuyau_bas,(x_tuyau,y_tuyau+509+ecart)) #509pix = taille tuyau

def bord_defile(bord,x_bord,y_bord):
    surface.blit(bord,(x_bord,y_bord))


def message(texte,surfaceL,surfaceH,son_gameover):
    gameover = pygame.font.Font("04b.ttf",140)
    gameoversurface, gameoverRect = creaTexte(texte, gameover) #contient 1 
                                                           #texte et 1 police
    gameoverRect.center = surfaceL/2, (surfaceH/2)-50
    surface.blit(gameoversurface, gameoverRect)
    son_gameover.play()
    pygame.display.update()
    rejoueQuit()

    
    
def creaTexte(texte, police):
    white = (255,255,255)
    textesurface = police.render(texte, True, white) # true : antialiasing
    return textesurface, textesurface.get_rect()



def rejoueQuit():
    time.sleep(1)
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                main()

def Score(score,x_tuyau):
    black = (0, 0, 0)    
    font = pygame.font.Font(None ,50)
    textesurface = font.render(("Score: "+str(score)), True, black) 
    #conversion en string pr concatener
    surface.blit(textesurface, [0, 0])

def collision(x,y,xf,yf,xt,yt,ecart,son_gameover):
    if x + xf > xt+20:
        if y < yt + 509-20:
            if x-xf < xt + 150-20:
                message("Game over",surfaceL,surfaceH,son_gameover)

    if x + xf > xt+20:
        if y + yf > yt + 509+ecart+20:
            if x-xf < xt + 150-20:
                message("Game over",surfaceL,surfaceH,son_gameover)

def gravity(y, gravity = 0.2):
    return y + gravity

def main(): 
    fond = pygame.image.load("fondflappy.png")
    oiseau = pygame.image.load("flappy2.png")
    tuyau = pygame.image.load("tuyau.png")
    bord = pygame.image.load("bord.png")
    tuyau_bas =  pygame.transform.rotate(tuyau, 180)
    x_flappy = 68
    y_flappy = 50
    rotate_flappy = 0
    x = 150
    y = 200
    y_mouv = -5
    x_tuyau = surfaceL
    y_tuyau = random.randint(-400,-280)
    ecart = 3*y_flappy
    tuyau_vitesse = 2
    score = 0
    x_bord = 16
    y_bord = 470
    son_saut = pygame.mixer.Sound("saut.wav")
    son_tuyau = pygame.mixer.Sound("tuyau.wav")
    son_gameover = pygame.mixer.Sound("gameover.wav")
    game_over = False
    while (game_over == False) :  #quitter boucle inf
        for event in pygame.event.get(): #recherche parmi evenements
            if event.type == pygame.QUIT:
                game_over = True 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    son_saut.play() 
                    if y > -5:
                        y_mouv = -5
                        rotate_flappy = 45
                    
            #if event.type == pygame.KEYUP:
            #    y_mouv = 3
        y += y_mouv

        if y>surfaceH-75: #2 bords en hauteur
            message("Game over",surfaceL,surfaceH,son_gameover)
        
        if x_tuyau < (0):
            x_tuyau =  surfaceL
            y_tuyau = random.randint(-400,-280)
            score +=1
            if score >= 3:
                ecart = 2*y_flappy
                tuyau_vitesse = score
                if score >= 10:
                    tuyau_vitesse = 10
        if x_tuyau == x:
            son_tuyau.play()

        surface.blit(fond,(0,0))         
        flappy(x,y, oiseau, rotate_flappy)
        tuyaux(tuyau,tuyau_bas,x_tuyau,y_tuyau, ecart)
        x_tuyau -= tuyau_vitesse # bouge de 6 pixels
        Score(score,x_tuyau)
        collision(x,y,x_flappy,y_flappy,x_tuyau,y_tuyau,ecart,son_gameover)

        if x_bord < -339 :
            x_bord = 16
        bord_defile(bord,x_bord,y_bord)
        x_bord -= tuyau_vitesse
        rotate_flappy -= 0.8
        y_mouv = gravity(y_mouv)
        pygame.display.update() #rafraichissement
        
        
        
main()
pygame.quit()
quit()