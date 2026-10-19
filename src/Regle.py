# Créé par thom.mauline, le 01/06/2023 en Python 3.7

from runtime import asset_path, launch_script

import pygame
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)

pygame.init()
pygame.mixer.music.load(asset_path("assets/Musiques/Musique_accueil.mp3"))
pygame.mixer.music.play()

# Définir la taille de la fenêtre (largeur, hauteur)
taille_fenetre = (1200, 600)
ecran = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("SuperTower")

# Afficher le fond à l'écran puis les règles
ecran.blit(pygame.transform.scale(pygame.transform.scale(pygame.image.load(asset_path("assets/Img/back.jpg")), taille_fenetre), taille_fenetre), (0, 0))
ecran.blit(pygame.transform.scale(pygame.transform.scale(pygame.image.load(asset_path("assets/Img/regles.png")), taille_fenetre), taille_fenetre), (0, 0))

# Afficher le bouton menu
ecran.blit(pygame.transform.scale(pygame.image.load(asset_path("assets/Img/main_menu.png")),(318, 72)), (441, 528))

# Mettre à jour l'affichage
pygame.display.flip()

a=0
continuer = True
#Boucle infinie pour faire le choix (il n'y a actuellement pas de choix à faire
while continuer :
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.rewind()
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            continuer = False
        if evenement.type == pygame.MOUSEBUTTONDOWN:
            #si on appuie sur le bouton, le jeux se lance
            if (441<=evenement.pos[0]) and (evenement.pos[0]<=759) and (528<=evenement.pos[1]) and (evenement.pos[1]<=600) and evenement.button == 1 :
                pygame.quit()
                launch_script("Menu.py")

pygame.quit()