# Créé par MaisonDoucam, le 17/01/2023 en Python 3.7

from runtime import asset_path
from pygame import *
from pygame.locals import *
from Fonctions_Diverses import *
from Attaques import *
from Déplacements import *

def chargement_Thomas():
    import pygame
    #Liste des images du personnage
    image_sprite = [[[pygame.image.load(asset_path("assets/Img/hero_walking_left_1.png")),
    pygame.image.load(asset_path("assets/Img/hero_walking_left_2.png")),
    pygame.image.load(asset_path("assets/Img/hero_walking_left_3.png")),
    pygame.image.load(asset_path("assets/Img/hero_walking_left_4.png")),
    pygame.image.load(asset_path("assets/Img/hero_walking_left_5.png")),
    pygame.image.load(asset_path("assets/Img/hero_walking_left_6.png")),
    pygame.image.load(asset_path("assets/Img/hero_walking_left_7.png")),
    pygame.image.load(asset_path("assets/Img/hero_walking_left_8.png")),
    pygame.image.load(asset_path("assets/Img/hero_walking_left_9.png"))],
    [pygame.image.load(asset_path("assets/Img/hero_walking_right_1.png")),
    pygame.image.load(asset_path("assets/Img/hero_walking_right_2.png")),
    pygame.image.load(asset_path("assets/Img/hero_walking_right_3.png")),
    pygame.image.load(asset_path("assets/Img/hero_walking_right_4.png")),
    pygame.image.load(asset_path("assets/Img/hero_walking_right_5.png")),
    pygame.image.load(asset_path("assets/Img/hero_walking_right_6.png")),
    pygame.image.load(asset_path("assets/Img/hero_walking_right_7.png")),
    pygame.image.load(asset_path("assets/Img/hero_walking_right_8.png")),
    pygame.image.load(asset_path("assets/Img/hero_walking_right_9.png"))]]]

    #Liste contenant les coordonnés (xgauche,xdroite,y) des surface sur lesquelles le perso peut se poser
    Plateformes=[(150,210,390),(0, 780, 120),(360,420, 360),(990,1050, 150),(30,120, 270),(960,1060, 510),(0,120, 510),(300,570, 240),(690,870, 240),(615,645, 240),(720,870, 420)]

    #Liste contenant les coordonnés (xgauche,xdroite,yhaut,ybas) des surface sur lesquelles le perso peut se poser
    Pièges=[pygame.Rect(0,457,60,53),pygame.Rect(690,560,180,40)]

    Projectiles=[pygame.image.load(asset_path("assets/Img/boulle_de_neige.png")),(pygame.image.load(asset_path("assets/Img/Fleche_gauche.png")),pygame.image.load(asset_path("assets/Img/Fleche_droite.png"))),
    (pygame.image.load(asset_path("assets/Img/boulle_de_feu_gauche.png")),pygame.image.load(asset_path("assets/Img/boulle_de_feu_droite.png")))]

    #Création du dictionnaire de thomas pour les données nécessaire au personnage :
    dico_perso={'x':1100,'y':550,'image':image_sprite[0][0][0],'ancienx':1110,'ancieny':540,'vies':3,
    'touche_pressée':[0 for a in range(280)],'avancement_action':0,'avancement_saut':0,'plateformes':[(25,200,520)],'banque_img':image_sprite,
    'projectile_list':[],'projectile_cooldown':0,'sens_image':0,'avancement_image':1,'type_action':0,'gravité?':True,'Touche_le_sol':False,
    'projectile_surfaces':Projectiles,'Plateformes':Plateformes,'Dangers':Pièges,'cooldown_dégat':0}
    return dico_perso

#Gestion des touches pressées
#dico_perso={'x','y','image','ancienx','ancieny','ancienimage',
#'touche_pressée','avancement_action','saut','projectile_list','projectile_cooldown'
#'sens_image','avancement_image','type_action'}
#Out:dico_perso mais modifié
def gestion_personnage(gpc,pnj):
    #On enregistre la position avant de la modifier
    gpc['ancienx']=gpc['x']
    gpc['ancieny']=gpc['y']
    #Est-ce que on touche le sol ?
    if plateforme(gpc['x'],gpc['y'],gpc['Plateformes'])==True or gpc['y']>=550:
        gpc['Touche_le_sol']=True
    else:
        gpc['Touche_le_sol']=False
    #Bloquage des actions si le personnage est en train de réaliser une animation de dégat
    if gpc['cooldown_dégat']>0:
        gpc['cooldown_dégat']-=1
    damage(gpc,pnj)
    if (gpc['avancement_action']>0 and gpc['type_action']==2) or damage(gpc,pnj)=='Dégat gauche':
        dégat_gauche(gpc)
    elif (gpc['avancement_action']>0 and gpc['type_action']==3) or damage(gpc,pnj)=='Dégat droite':
        dégat_droite(gpc)
    else:
        #Si il y a des projectiles dans la liste
        if gpc['projectile_cooldown']!=0:
            gpc['projectile_cooldown']-=1
        if gpc['projectile_list']!=[]:
            gestion_sort(gpc)
        #Si la touche "Q","S" ou "X" est pressée, on lance un sort
        if gpc['touche_pressée'][97]==1 or gpc['touche_pressée'][115]==1 or gpc['touche_pressée'][120]==1 :
            sort(gpc)
        #Si un saut est en cours, on entre dans la boucle du saut
        if gpc['avancement_saut']!=0:
            jump(gpc)
        #Si une des flèches est pressée
        if gpc['touche_pressée'][K_RIGHT]==1 or gpc['touche_pressée'][K_LEFT]==1 or gpc['touche_pressée'][K_UP]==1:
            mouvement_perso(gpc)
        #Remise du cycle d'image d'animation à zéro
        if gpc['avancement_image']>9:
            gpc['avancement_image']=1
    if plateforme(gpc['x'],gpc['y'],gpc['Plateformes'])==False:
        gravité(gpc)
    #Blocage des limites de la fenêtre
    if gpc['x']<0 or gpc['x']>1160:
        gpc['x']=gpc['ancienx']
    if gpc['y']<=0 or (146<gpc['y']<154 and 0<gpc['x']<780):
        gpc['y']=gpc['ancieny']
    import pygame
    if gpc['sens_image']==0:
        gpc['image']=pygame.image.load(asset_path("assets/Img/hero_walking_left_"+str(gpc['avancement_image'])+".png"))
    else:
        gpc['image']=pygame.image.load(asset_path("assets/Img/hero_walking_right_"+str(gpc['avancement_image'])+".png"))
    return gpc['x'],gpc['y'],gpc['image']


