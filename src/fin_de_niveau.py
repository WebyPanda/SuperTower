# Créé par MaisonDoucam, le 31/05/2023 en Python 3.7

from runtime import asset_path, launch_script

import pygame
from pygame.locals import *
from CmdMoove import *
from Fonctions_Diverses import *
from Attaques import*
from Déplacements import*

def mort(window,run,niveau):
        import pygame
        #Affichage du choix
        window.blit(pygame.transform.scale(pygame.image.load(asset_path("assets/Img/main_menu.png")),(318, 72)), (441, 300))
        window.blit(pygame.transform.scale(pygame.image.load(asset_path("assets/Img/bt-play.png")),(318, 72)), (441, 189))
        pygame.display.flip()
        #boucle infini en attendant le choix
        while run:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    #on arrete
                    pygame.quit()
                    raise SystemExit(0)
                elif evenement.type == pygame.MOUSEBUTTONDOWN:
                    if 441<=evenement.pos[0]<=759 and 189<=evenement.pos[1]<=261 and evenement.button == 1 :
                        #on recommence en quittant puis relisant le fichier du jeux comme si rien n'était arrivé
                        pygame.quit()
                        if niveau=="niveau1":
                            launch_script("Jeux.py")
                        if niveau=="niveauboss":
                            launch_script("NiveauFinal.py")
                    elif 441<=evenement.pos[0]<=759 and 300<=evenement.pos[1]<=372 and evenement.button == 1:
                        #on retourne au menu en quittant puis relisant le fichier du menu comme si rien n'était arrivé
                        pygame.quit()
                        launch_script("Menu.py")

def win(window,run):
        import pygame
        #Affichage du choix
        window.blit(pygame.transform.scale(pygame.image.load(asset_path("assets/Img/next_level.png")),(318, 72)), (441, 189))
        pygame.display.flip()
        #boucle infini en attendant le choix
        while run:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    #on arrete
                    pygame.quit()
                    raise SystemExit(0)
                elif evenement.type == pygame.MOUSEBUTTONDOWN:
                    if 441<=evenement.pos[0]<=759 and 189<=evenement.pos[1]<=261 and evenement.button == 1 :
                            pygame.quit()
                            launch_script("NiveauFinal.py")

def fin_du_jeu(compteur,gpc,fin):
    import pygame
    if compteur<16:
        compteur+=1
    else:
        compteur=1
    image=pygame.transform.scale(pygame.image.load(asset_path("assets/image_etoile/ZNec_frame_"+str(compteur)+".png")),(100, 100))
    étoile_rect=pygame.Rect(15,490,100,100)
    perso_rect=pygame.Rect(gpc['x'],gpc['y'],gpc['image'].get_width(),gpc['image'].get_height())
    if fin==False:
        if perso_rect.colliderect(étoile_rect)==True:
            fin=True
    return image,compteur,fin
