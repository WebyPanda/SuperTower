# Docstrings,
from pygame import *
from pygame.locals import *
#Gravité
def gravité(gpc_gravité):
    #Si la gravité est activée et que on est au dessus de la hauteur de sol, on baisse en hauteur jusu'à atteindre le niveau du sol
    if gpc_gravité['y']<550 and gpc_gravité['gravité?']==True:
        gpc_gravité['y']+=7
    #Si on est en dessous du niveau du sol, on se met au niveau du sol
    if gpc_gravité['y']>550 :
        gpc_gravité['y']=550

#renvoie la position du personnage (qui va vers la gauche) tant que le compteur n'a pas atteint 0 (la condition est exprimée avant le lancement de la fonction)
def dégat_droite(gpc_chute):
    gpc_chute['avancement_action']-=10
    gpc_chute['y']+=5/100*gpc_chute['avancement_action']*(gpc_chute['avancement_action']-200)-(5/100*(gpc_chute['avancement_action']+1)*((gpc_chute['avancement_action']+1)-200))
    gpc_chute['x']-=10

#renvoie la position du personnage (qui va vers la droite) tant que le compteur n'a pas atteint 0
def dégat_gauche(gpc_chute):
    gpc_chute['avancement_action']-=10
    gpc_chute['y']+=5/100*gpc_chute['avancement_action']*(gpc_chute['avancement_action']-200)-(5/100*(gpc_chute['avancement_action']+1)*((gpc_chute['avancement_action']+1)-200))
    gpc_chute['x']+=10

#Est-ce que l'objet touche le sol ?
def plateforme(x,y,liste):
    #On prend les tuples ayants les coordonnées des plateformes
    for elt in liste:
        #On compare les x et les y avec ceux de l'objet
        if elt[0]-4<x+20<elt[1]+4 and (elt[2]-4)<(y+50)<(elt[2]+4):
        #Réponses à la question
            return True
    return False

#Est-ce que l'objet subit des dégats ?
def damage(gpc,pnj):
    import pygame
    #Si on a pas pris de dégat dans les dernières secondes (de sorte qu'on se soit pas bloqué entre un monstre et des pics sans pouvoir s'échapper)
    if gpc['cooldown_dégat']<=0:
        #Remise à neuf de la liste contenant des dangers pour le personnage, en y mettant les coordonnées des dangers immobiles (les pics)

        #Ajoute dans la liste des dangers potentiels les coordonnées des enemis
        for key in pnj.keys():
            if (key=='monstre1'  or key=='monstre2' or key=='monstre3') and pnj[key]['réaparition_dans']==0:
                rect=pygame.Rect(pnj[key]['x'],pnj[key]['y'],pnj[key]['image'].get_width(),pnj[key]['image'].get_height())
                gpc['Dangers'].append(rect)
            elif key=='flèche1'  or key=='flèche2' or key=='boss':
                rect=pygame.Rect(pnj[key]['x'],pnj[key]['y'],pnj[key]['image'].get_width(),pnj[key]['image'].get_height())
                gpc['Dangers'].append(rect)
        perso_rect=pygame.Rect(gpc['x'],gpc['y'],gpc['image'].get_width(),gpc['image'].get_height())
        #On prend les tuples ayants les coordonnées des dangers
        for elt in gpc['Dangers']:
            #Si on touche des dangers par la gauche
            if perso_rect.colliderect(elt):
                if abs(perso_rect.left-elt.right)<=20 or abs(perso_rect.top-elt.bottom)<20:
                #Mise à jour des compteurs pour l'animation, baisse de la vie, et compteurs d'attente avant de pouvoir reprendre un dégat
                    gpc['avancement_action']=211
                    gpc['type_action']=2
                    gpc['avancement_saut']=1
                    gpc['vies']-=1
                    gpc['cooldown_dégat']=60
                    return 'Dégat gauche'
            #Si on touche des dangers par la droite
                elif abs(perso_rect.right-elt.left)<=20 or abs(perso_rect.bottom-elt.top)<20:
                    #Mise à jour des compteurs pour l'animation, baisse de la vie, et compteurs d'attente avant de pouvoir reprendre un dégat
                    gpc['avancement_action']=211
                    gpc['type_action']=3
                    gpc['avancement_saut']=1
                    gpc['vies']-=1
                    gpc['cooldown_dégat']=60
                    return 'Dégat droite'
    return False