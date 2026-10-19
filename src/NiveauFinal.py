# Créé par MaisonDoucam, le 31/05/2023 en Python 3.7
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
from boss_random import*
from fin_de_niveau import*

#Placement et bloquage de la position de la fenêtre
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)

# Initiate pygame and give permission
# to use pygame's functionality
pygame.init()
pygame.mixer.music.load(asset_path("assets/Musiques/Musique_fin.mp3"))
pygame.mixer.music.play()

# Create a display surface object
# of specific dimension
window = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("SuperTower")

# Création d'une horloge pour suivre le temps
clock = pygame.time.Clock()

#Création du disctionnaire necessaire aux mouvements du personnage et du boss
dico_perso=chargement_Thomas()

dico_boss={'boss':{'x':500,'y':527,'image':pygame.transform.scale(pygame.image.load(asset_path("assets/Images/Monstre 2 position 8.png")), (51,73)),
'sens':"",'anim':0,'vie':100,'deplacement_horizontal':0,'total_deplacement':0}}

#Création du boléen pour la boucle
run = True
#Temps d'attente avant le début du niveau le temps que le programme se lance à plein régime
temps_attente=50
win=0
fin=False
# Boucle infini pour faire tourner le jeu
while run:
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.rewind()
	#Limiter la fréquence d'image à 60 pour avoir un bon résultat
    clock.tick(45)
    #Remise en place du fond
    window.fill((0, 0, 0))
    window.blit(pygame.transform.scale(pygame.image.load(asset_path("assets/Img/Fond_moyen_age.jpg")), (1200, 600)), (0, 0))
    #Affichage des vies
    window.blit(pygame.image.load(asset_path("assets/Img/coeur_"+str(dico_perso['vies'])+".png")), (1030, 10))
    #Timer avant début
    if temps_attente>0:
        temps_attente-=1
        pygame.font.init()
        window.blit((pygame.font.SysFont('Agency Fb', 100)).render(str(temps_attente), False, (52,247,247 )), (530,250))
    if -20<temps_attente<=0:
        window.blit((pygame.font.SysFont('Agency Fb', 100)).render("!!!!!!!!GO!!!!!!!!!", False, (0,204,0)), (375,250))
        temps_attente-=1

    #Commandes du perso
    for event in pygame.event.get():
        dico_perso['touche_pressée'] = pygame.key.get_pressed()
        if event.type == QUIT:
             pygame.quit()
             raise SystemExit(0)
    if temps_attente<=0:
        #Compteur temps de survie (pour record)
        temps_attente-=1
        window.blit((pygame.font.SysFont('Agency Fb', 100)).render(str(-(temps_attente//60)), False, (52,247,247 )), (0,0))
        #Gestion du boss
        if win==0:
            deplacement_aleatoire(dico_boss)
            boss_damage(dico_boss,dico_perso)
            print(dico_boss)
        if win==0 and dico_boss['boss']['vie']<=0:
            pygame.mixer.music.load(asset_path("assets/Musiques/Musique_victoire.mp3"))
            pygame.mixer.music.play()
            x_boss,y_boss=dico_boss['boss']['x'],dico_boss['boss']['y']
            compteur=1
            win=1
            dico_boss={'boss':{'x':0,'y':0,'image':pygame.transform.scale(pygame.image.load(asset_path("assets/Images/Monstre 2 position 8.png")), (51,73)),
            'sens':"",'anim':0,'vie':0,'deplacement_horizontal':0,'total_deplacement':0}}
##        elif win==1 or dico_boss['boss']['vie']<=0:

        #Gestion du personnage et de ses actions et des projectiles
        if fin==False:
            x,y,image=gestion_personnage(dico_perso,dico_boss)
            dico_perso['Dangers'],dico_perso['Plateformes']=[],[]

        #Affichage du boss
        if win==0:
            window.blit(dico_boss['boss']['image'],(dico_boss['boss']['x'],dico_boss['boss']['y']))
        if win==1:
            window.blit(dico_boss['boss']['image'],(x_boss,y_boss))

        if win==1:
            image_étoile,compteur,fin=fin_du_jeu(compteur,dico_perso,fin)
            window.blit(image_étoile,(15,490))
            if fin==True:
                window.blit((pygame.font.SysFont('Agency Fb', 100)).render("!!!!!Victoire!!!!!!", False, (250,210,10)), (350,250))
        #Affichage des projectiles
        for bullet in dico_perso['projectile_list']:
            window.blit(bullet[4], bullet[4].get_rect(center = (bullet[0],bullet[1])))

        #Affichage du joueur
        window.blit(image, (x, y))

    #Chargement du nouvel écran
    pygame.display.flip()
    #Mort du personnage : recommencer ou quitter
    if dico_perso['vies']<=(0):
        mort(window,run,"niveauboss")
#Si la boucle s'arrete
pygame.quit()
