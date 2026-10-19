# Docstrings, OK
# Importing the modules
import pygame
from pygame.locals import *
from CmdMoove import *
from Fonctions_Diverses import *
from Attaques import*
from Déplacements import*
from Fond import*
from Gestion_Monstre import*

#Placement et bloquage de la position de la fenêtre
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)

# Initiate pygame and give permission
# to use pygame's functionality
pygame.init()

# Create a display surface object
# of specific dimension
window = pygame.display.set_mode((1200, 600))

# Création d'une horloge pour suivre le temps
clock = pygame.time.Clock()

#Création du disctionnaire necessaire aux mouvements du personnage
dico_perso=chargement_Thomas()

dico_pnj={'monstre1':{'x':0,'y':60,'image':pygame.transform.scale(pygame.image.load("Images/Monstre1position5.png"), (52,37)),'sens':0,'anim':0,'vie':5,'réaparition_dans':0},
'monstre2':{'x':0,'y':548,'image':pygame.transform.scale(pygame.image.load("Images/monstre 2 position 8.png"), (37,52)),'sens':0,'anim':0,'vie':5,'réaparition_dans':0},
'monstre3':{'x':1020,'y':461,'image':pygame.transform.rotate(pygame.image.load("Images/Monstre1position5.png"),90),'sens':0,'anim':0,'vie':5,'réaparition_dans':0},
'flèche1':{'x':30,'y':190,'image':pygame.image.load("Images/Flecheposition1.png")},
'flèche2':{'x':410,'y':370,'image':pygame.image.load("Images/Flecheposition1.png")}}

#Création du boléen pour la boucle
run = True
#Temps d'attente avant le début du niveau le temps que le programme se lance à plein régime
temps_attente=50
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
             exit()
    if temps_attente<=0:
        #Gestion des pnj et de leurs actions
        dico_pnj=gestion_monstres(dico_pnj,dico_perso)

        #Gestion du personnage et de ses actions et des projectiles
        x,y,image=gestion_personnage(dico_perso,dico_pnj)

        #Affichage des pnj
        for key in dico_pnj.keys():
            if key=='monstre1' or key=='monstre2' or key=='monstre3':
                print(dico_pnj[key],key)
                if dico_pnj[key]['réaparition_dans']==0:
                    window.blit(dico_pnj[key]['image'],(dico_pnj[key]['x'],dico_pnj[key]['y']))
                else:
                    dico_pnj[key]['réaparition_dans']-=1
            else:
                window.blit(dico_pnj[key]['image'],(dico_pnj[key]['x'],dico_pnj[key]['y']))

        #Affichage des projectiles
        for bullet in dico_perso['projectile_list']:
            window.blit(bullet[4], bullet[4].get_rect(center = (bullet[0],bullet[1])))

        #Affichage du joueur
        window.blit(image, (x, y))

	   #Chargement du nouvel écran
        pygame.display.flip()
    #Mort du personnage : recommencer ou quitter
    if dico_perso['vies']<=(0):
        fond(window,dico_perso,temps_attente)
        #Affichage du choix
        window.blit(pygame.transform.scale(pygame.image.load("Img\main_menu.png"),(318, 72)), (441, 300))
        window.blit(pygame.transform.scale(pygame.image.load("Img/bt-play.png"),(318, 72)), (441, 189))
        pygame.display.flip()
        #boucle infini en attendant le choix
        while run:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    #on arrete
                    pygame.quit()
                    exit()
                elif evenement.type == pygame.MOUSEBUTTONDOWN:
                    if 441<=evenement.pos[0]<=759 and 189<=evenement.pos[1]<=261 and evenement.button == 1 :
                        #on recommence en quittant puis relisant le fichier du jeux comme si rien n'était arrivé
                        pygame.quit()
                        os.system('C:\Edupython\App\python.exe "Jeux.py"')
                        os.system('python.exe "Jeux.py"')
                    elif 441<=evenement.pos[0]<=759 and 300<=evenement.pos[1]<=372 and evenement.button == 1:
                        #on retourne au menu en quittant puis relisant le fichier du menu comme si rien n'était arrivé
                        pygame.quit()
                        os.system('C:\Edupython\App\python.exe "Menu.py"')
                        os.system('python.exe "Menu.py"')
#Si la boucle s'arrete
pygame.quit()
exit()