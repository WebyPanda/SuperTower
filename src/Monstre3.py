from runtime import asset_path
import pygame
from pygame.locals import *
pygame.init()



def gerer_monstre3(sous_dico):

    """
    Fonction qui prend en paramètres la position du monstre, la variable de changement de sens , l'image du monstre, et la variable d'animation.
    Cette fonction gère le déplacement du monstre, si il doit aller vers le haut, vers le bas et son animation (légère)
    """
    xmonstre3,ymonstre3,imonstre3,monstre3,animmonstre3,viemonstre3=sous_dico['x'],sous_dico['y'],sous_dico['sens'],sous_dico['image'],sous_dico['anim'],sous_dico['vie']
    if imonstre3 == 0 :  #Si la variable de changement de sens est égale à 0 , alors :
        ymonstre3=ymonstre3-1.2  #Le monstre bouge
#Boucles pour l'animation :
        if animmonstre3 <20 :
            animmonstre3+=1
        elif animmonstre3 == 20:
            monstre3 = pygame.image.load(asset_path("assets/Images/Monstre1position5.png"))
            monstre3 = pygame.transform.rotate(monstre3,90)
            animmonstre3+=1

        if 20 < animmonstre3 <40 :
            animmonstre3+=1
        elif animmonstre3 == 40 :
            monstre3 = pygame.image.load(asset_path("assets/Images/Monstre1position6.png"))
            monstre3 = pygame.transform.rotate(monstre3,90)
            animmonstre3+=1

        if 40 < animmonstre3 < 60 :
            animmonstre3+=1
        elif animmonstre3 == 60 :
            monstre3 = pygame.image.load(asset_path("assets/Images/Monstre1position7.png"))
            monstre3 = pygame.transform.rotate(monstre3,90)
            animmonstre3+=1

        if 60 < animmonstre3 < 80 :
            animmonstre3+=1
        elif animmonstre3 == 80 :
            monstre3 = pygame.image.load(asset_path("assets/Images/Monstre1position8.png"))
            monstre3 = pygame.transform.rotate(monstre3,90)
            animmonstre3=0
#Boucle pour appeller le else de la fonction pour permettre le retour du monstre dans l'autre sens :
        if ymonstre3 <= 213 :
            imonstre3 = 1
            animmonstre3 = 0
            monstre3 = pygame.image.load(asset_path("assets/Images/Monstre1position1.png"))
            monstre3 = pygame.transform.rotate(monstre3,270)
    else:

        ymonstre3=ymonstre3+1.2
#Boucles pour l'animation :
        if animmonstre3 <20:
            animmonstre3+=1
        elif animmonstre3 == 20 :
            monstre3 = pygame.image.load(asset_path("assets/Images/Monstre1position1.png"))
            monstre3 = pygame.transform.rotate(monstre3,270)
            animmonstre3+=1

        if 20 < animmonstre3 < 40 :
            animmonstre3+=1
        elif animmonstre3 == 40 :
            monstre3 = pygame.image.load(asset_path("assets/Images/Monstre1position2.png"))
            monstre3 = pygame.transform.rotate(monstre3,270)
            animmonstre3+=1

        if 40 < animmonstre3 < 60 :
            animmonstre3+=1
        elif animmonstre3 == 60:
            monstre3 = pygame.image.load(asset_path("assets/Images/Monstre1position3.png"))
            monstre3 = pygame.transform.rotate(monstre3,270)
            animmonstre3+=1

        if 60 < animmonstre3 < 80 :
            animmonstre3+=1
        elif animmonstre3 == 80 :
            monstre3 = pygame.image.load(asset_path("assets/Images/Monstre1position4.png"))
            monstre3 = pygame.transform.rotate(monstre3,270)
            animmonstre3=0
#Boucle pour appeller le if de la fonction pour permettre le retour du monstre dans l'autre sens :
        if ymonstre3 >= 463 :
            imonstre3 = 0
            animmonstre3 = 0
            monstre3 = pygame.image.load(asset_path("assets/Images/Monstre1position5.png"))
            monstre3 = pygame.transform.rotate(monstre3,90)

    sous_dico['x'],sous_dico['y'],sous_dico['sens'],sous_dico['image'],sous_dico['anim'],sous_dico['vie']=xmonstre3,ymonstre3,imonstre3,monstre3,animmonstre3,viemonstre3
    return sous_dico