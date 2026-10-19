# Docstrings, OK
# Importing the modules

from runtime import asset_path

import pygame
from pygame.locals import *
from CmdMoove import *
from Fonctions_Diverses import *
from Attaques import*
from Déplacements import*
from Fond import*
from Gestion_Monstre import*
from fin_de_niveau import*

#Placement et bloquage de la position de la fenêtre
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)

# Initiate pygame and give permission
# to use pygame's functionality
pygame.init()
pygame.mixer.music.load(asset_path("assets/Musiques/Musique_Jeu.mp3"))
pygame.mixer.music.play()

# Create a display surface object
# of specific dimension
window = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("SuperTower")

# Création d'une horloge pour suivre le temps
clock = pygame.time.Clock()

#Création du disctionnaire necessaire aux mouvements du personnage et des monstres
dico_perso,dico_pnj=chargement_Thomas(),chargement_Baptiste()

#Création du boléen pour la boucle
run = True
#Temps d'attente avant le début du niveau le temps que le programme se lance à plein régime
temps_attente=150
# Boucle infini pour faire tourner le jeu
while run:
	#Limiter la fréquence d'image à 60 pour avoir un bon résultat
    clock.tick(45)
    #Remise en place du fond
    temps_attente=fond(window,dico_perso,temps_attente)

    #Commandes du perso
    for event in pygame.event.get():
        dico_perso['touche_pressée'] = pygame.key.get_pressed()
        if event.type == QUIT:
             pygame.quit()
             raise SystemExit(0)
    if temps_attente<=0:
        #Gestion des pnj et de leurs actions
        dico_pnj=gestion_monstres(dico_pnj,dico_perso)

        #Gestion du personnage et de ses actions et des projectiles
        dico_perso['Dangers']=[pygame.Rect(0,457,60,53),pygame.Rect(690,560,180,40)]
        x,y,image=gestion_personnage(dico_perso,dico_pnj)

        #Affichage des pnj
        for key in dico_pnj.keys():
            if key=='monstre1' or key=='monstre2' or key=='monstre3':
                #s'ils ne sont pas morts
                if dico_pnj[key]['réaparition_dans']==0:
                    window.blit(dico_pnj[key]['image'],(dico_pnj[key]['x'],dico_pnj[key]['y']))
                #Sinon on baisse le temps avant la réaparition
                else:
                    dico_pnj[key]['réaparition_dans']-=1
            #Si c une flèche
            else:
                window.blit(dico_pnj[key]['image'],(dico_pnj[key]['x'],dico_pnj[key]['y']))

        #Affichage des projectiles
        for bullet in dico_perso['projectile_list']:
            window.blit(bullet[4], bullet[4].get_rect(center = (bullet[0],bullet[1])))

        #Affichage du joueur
        window.blit(image, (x, y))

    #Chargement du nouvel écran
    pygame.display.flip()
    rect_perso=pygame.Rect(dico_perso['x'],dico_perso['y'],dico_perso['image'].get_width(),dico_perso['image'].get_height())
    if rect_perso.colliderect(pygame.Rect(10,20,75,100))==True:
        win(window,run)
    #Mort du personnage : recommencer ou quitter
    if dico_perso['vies']<=(0):
        fond(window,dico_perso,temps_attente)
        mort(window,run,"niveau1")
#Si la boucle s'arrete
pygame.quit()