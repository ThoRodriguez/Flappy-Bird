# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:31:35 2015

@author: Thomas Rodriguez et Maxime Thibert

Pour jouer, appuyez une fois sur ESPACE (nouvelle partie ou si vous mourrez)
Une seule touche est nécéssaire pour voler : la touche ESPACE.

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
    '''
    Fonction qui permet de replacer le sol à sa position de départ après
    avoir défilé
    ---
    Paramètres :
    
    bord : img
    x_bord : int
    y_bord : int
    Valeurs calculées pour un défilement fluide
    ---
    Retourne un entier (coordonnée x du sol)
    
    '''
    surface.blit(bord,(x_bord,y_bord))
    if x_bord < -339 :
        x_bord = 16
    return x_bord

def message(texte,surfaceL,surfaceH,son_gameover):
    '''
    Fonction qui affiche le message Game over et appelle la fonction
    rejoueQuit 
    '''
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
    '''
    Fonction qui permet de relancer la partie ou quitter
    '''
    time.sleep(1)
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                main()

def Score(score,x_tuyau,x,son):
    black = (0, 0, 0)    
    font = pygame.font.Font(None ,50)
    textesurface = font.render(("Score: "+str(score)), True, black) 
    #conversion en string pr concatener
    surface.blit(textesurface, [0, 0])
    if (score < 5):
        if x_tuyau == x+1 or x_tuyau == x-1  :
            son.play()
            score +=1
        
    if (5 <= score <10):
        if (x_tuyau == x+5):
            son.play()
            score +=1
            
    if (score >= 10):
        if (x_tuyau == x+10):
            son.play()
            score +=1
            
    return score

def collision(x,y,xf,yf,xt,yt,ecart,son_gameover):
    '''
    Fonction qui gère les collisions
    ---
    Paramètres : 
    x,y,xf,yf,xt,yt,ecart : int
    
    son_gameover : fichier son
    ---
    Vérifie les différentes conditions pour perdre au jeu et appelle
    la fonction message() si une d'elles vérifiée
    
    '''
    if x + xf > xt+20:
        if y < yt + 509-20:
            if x-xf < xt + 150-20:
                message("Game over",surfaceL,surfaceH,son_gameover)

    if x + xf > xt+20:
        if y + yf > yt + 509+ecart+20:
            if x-xf < xt + 150-20:
                message("Game over",surfaceL,surfaceH,son_gameover)


    if y>surfaceH-75: 
            message("Game over",surfaceL,surfaceH,son_gameover)


def gravity(y, gravity = 0.2):#gravity:paramètre facultatif car déjà initialisé 
    return y + gravity


def difficulte(score,tv):
    '''
    Fonction qui gère la difficulté (simule les levels)
    ---
    Paramètres :
    score : int
    tv : int
    ---
    Retourne : int
    
    '''
    if score >= 5:
        tv = 5
    if score >= 10:
        tv = 10
    return tv


def menu():
    '''
    Fonction qui affiche le menu, ne lance le jeu que si on appuie sur
    la barre espace (et appelle ainsi la fonction main)
    Arguments : 
    fond_menu : img
    play et continuer : rôle de booléens
    '''
    fond_menu = pygame.image.load("menu.jpg")
    play = 0
    continuer = True

    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
                play = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                play = 1
                continuer = False

        surface.blit(fond_menu, (0, 0))
        pygame.display.flip()
    if play == 1:
            return main()
    else:
        pygame.quit()
        quit()

def main(): 
    fond = pygame.image.load("fondflappy.png")
    oiseau = pygame.image.load("flappy2.png")
    tuyau = pygame.image.load("tuyau.png")
    tuyau_bas =  pygame.transform.rotate(tuyau, 180)
    bord = pygame.image.load("bord.png")
    x_flappy = 68
    y_flappy = 50
    rotate_flappy = 0
    x = 150
    y = 200
    y_mouv = -5
    x_tuyau = surfaceL
    y_tuyau = random.randint(-400,-280)
    ecart = 3*y_flappy
    tuyau_vitesse = 3
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
        # si le joueur est au dessus de l'écran on peut plus le faire sauter
                        y_mouv = -5
                        rotate_flappy = 45

        y += y_mouv

        
        if x_tuyau < (0):
            x_tuyau =  surfaceL
            y_tuyau = random.randint(-400,-280)
    

        
        surface.blit(fond,(0,0))         
        flappy(x,y, oiseau, rotate_flappy)
        tuyaux(tuyau,tuyau_bas,x_tuyau,y_tuyau, ecart)
        x_tuyau -= tuyau_vitesse

        score = Score(score,x_tuyau,x,son_tuyau)
        collision(x,y,x_flappy,y_flappy,x_tuyau,y_tuyau,ecart,son_gameover)
        tuyau_vitesse = difficulte(score,tuyau_vitesse)

        
        x_bord = bord_defile(bord,x_bord,y_bord)
        x_bord -= tuyau_vitesse
        rotate_flappy -= 0.8 # on augmente l'angle de rotation
        y_mouv = gravity(y_mouv) 
        # On augmente la vitesse de la chute à chaque tour de boucle
        pygame.display.update() #rafraichissement
        
        
        
menu()
pygame.quit()
quit()