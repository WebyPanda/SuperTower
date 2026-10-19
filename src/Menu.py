# Si "No module named 'pygame'" s'affiche, il faut installer pygame avec la commande "python -m pip install pygame" dans le terminal

import sys

from runtime import asset_path, launch_script, run_game

import pygame
import os

if "--verify-bundle" in sys.argv:
    try:
        pygame.image.load(asset_path("assets/Img/back.jpg"))
        pygame.image.load(asset_path("assets/Img/main_menu.png"))
        pygame.image.load(asset_path("assets/Img/regles.png"))
        pygame.image.load(asset_path("assets/Img/Fond_moyen_age.jpg"))
        pygame.image.load(asset_path("assets/Img/hero_walking_left_1.png"))

        pygame.mixer.init()
        pygame.mixer.music.load(asset_path("assets/Musiques/Musique_accueil.mp3"))
        pygame.mixer.music.load(asset_path("assets/Musiques/Musique_Jeu.mp3"))
        pygame.mixer.music.load(asset_path("assets/Musiques/Musique_fin.mp3"))
        pygame.mixer.music.load(asset_path("assets/Musiques/Musique_victoire.mp3"))
    finally:
        pygame.quit()
    raise SystemExit(0)

if __name__ == "__main__":
    run_game("Menu.py")
    raise SystemExit(0)

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)

pygame.init()
pygame.mixer.music.load(asset_path("assets/Musiques/Musique_accueil.mp3"))
pygame.mixer.music.play()

# Définir la taille de la fenêtre (largeur, hauteur)
taille_fenetre = (1200, 600)
ecran = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("SuperTower")

# Afficher le fond à l'écran
ecran.blit(pygame.transform.scale(pygame.transform.scale(pygame.image.load(asset_path("assets/Img/back.jpg")), taille_fenetre), taille_fenetre), (0, 0))

# Afficher le bouton règles
ecran.blit(pygame.transform.scale(pygame.image.load(asset_path("assets/Img/rules button.png")),(318, 72)), (441, 300))

# Afficher le bouton play
ecran.blit(pygame.transform.scale(pygame.image.load(asset_path("assets/Img/bt-play.png")),(318, 72)), (441, 189))

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
            if (441<=evenement.pos[0]) and (evenement.pos[0]<=759) and (189<=evenement.pos[1]) and (evenement.pos[1]<=261) and evenement.button == 1 :
                pygame.quit()
                launch_script("Jeux.py")
            if (441<=evenement.pos[0]) and (evenement.pos[0]<=759) and (300<=evenement.pos[1]) and (evenement.pos[1]<=372) and evenement.button == 1 :
                pygame.quit()
                launch_script("Regle.py")

pygame.quit()