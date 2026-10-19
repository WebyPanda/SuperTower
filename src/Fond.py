# Docstrings, OK
from runtime import asset_path
import pygame
from pygame.locals import *

def fond(window,dico,temps_attente):
    #Remet l'écran à zéro anvant de tout réafficher au bon endroit
    window.fill((0, 0, 0))

    #Affichage du fond d'écran
    background = pygame.transform.scale(pygame.image.load(asset_path("assets/Img/Fond_moyen_age.jpg")), (1200, 600))
    window.blit(pygame.transform.scale(pygame.image.load(asset_path("assets/Img/Fond_moyen_age.jpg")), (1200, 600)), (0, 0))

    #Affichage des Blocs et pics
    window.blit(pygame.image.load(asset_path("assets/Img/4.jpg")), (150, 390))
    window.blit(pygame.image.load(asset_path("assets/Img/5.jpg")), (0, 120))
    window.blit(pygame.image.load(asset_path("assets/Img/4.jpg")), (360, 360))
    window.blit(pygame.image.load(asset_path("assets/Img/4.jpg")), (990, 150))
    window.blit(pygame.image.load(asset_path("assets/Img/6.jpg")), (30, 270))
    window.blit(pygame.image.load(asset_path("assets/Img/6.jpg")), (960, 510))
    window.blit(pygame.image.load(asset_path("assets/Img/7.jpg")), (0, 510))
    window.blit(pygame.image.load(asset_path("assets/Img/11.jpg")), (300, 240))
    window.blit(pygame.image.load(asset_path("assets/Img/10.jpg")), (690, 240))
    window.blit(pygame.image.load(asset_path("assets/Img/9.jpg")), (615, 240))
    window.blit(pygame.image.load(asset_path("assets/Img/8.jpg")), (720, 420))
    window.blit(pygame.image.load(asset_path("assets/Img/PIC.png")), (0, 457))
    window.blit(pygame.image.load(asset_path("assets/Img/PIC 4.png")), (690, 560))

    #Affichage de la porte et son rectangle de collision
    window.blit(pygame.transform.scale(pygame.image.load(asset_path("assets/Img/porte_boss.png")), (75, 100)), (10, 20))

    #Affichage des vies
    window.blit(pygame.image.load(asset_path("assets/Img/coeur_"+str(dico['vies'])+".png")), (1030, 10))

    #baisse progressive du temps d'attente avant le début
    if temps_attente>0:
        temps_attente-=1
        pygame.font.init()
        window.blit((pygame.font.SysFont('Agency Fb', 100)).render(str(temps_attente), False, (52,247,247 )), (530,250))
    if -20<temps_attente<=0:
        window.blit((pygame.font.SysFont('Agency Fb', 100)).render("!!!!!!!!GO!!!!!!!!!", False, (0,204,0)), (375,250))
        temps_attente-=1
    return temps_attente