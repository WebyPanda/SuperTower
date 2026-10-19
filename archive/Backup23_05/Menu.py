import pygame
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)

pygame.init()

# Définir la taille de la fenêtre (largeur, hauteur)
taille_fenetre = (1200, 600)
ecran = pygame.display.set_mode(taille_fenetre)

# Afficher le fond à l'écran
ecran.blit(pygame.transform.scale(pygame.transform.scale(pygame.image.load("Img/back.jpg"), taille_fenetre), taille_fenetre), (0, 0))

# Afficher le bouton règles
##ecran.blit(pygame.transform.scale(pygame.image.load("K/rules button.png"),(318, 72)), (441, 300))

# Afficher le bouton play
ecran.blit(pygame.transform.scale(pygame.image.load("Img/bt-play.png"),(318, 72)), (441, 189))

# Mettre à jour l'affichage
pygame.display.flip()

a=0
continuer = True
#Boucle infinie pour faire le choix (il n'y a actuellement pas de choix à faire
while continuer :
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            continuer = False
        if evenement.type == pygame.MOUSEBUTTONDOWN:
            #si on appuie sur le bouton, le jeux se lance
            if (441<=evenement.pos[0]) and (evenement.pos[0]<=759) and (189<=evenement.pos[1]) and (evenement.pos[1]<=261) and evenement.button == 1 :
                import os
                pygame.quit()
                os.system('C:\Edupython\App\python.exe "Jeux.py"')
                os.system('python.exe "Jeux.py"')

pygame.quit()
quit()