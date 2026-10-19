import pygame
from pygame.locals import *
pygame.init()



def gerer_monstre1(sous_dico):

    """
    Fonction qui prend en paramètres la position du monstre, la variable de changement de sens , l'image du monstre, et la variable d'animation.
    Cette fonction gère le déplacement du monstre, si il doit aller vers la droite, la gauche, et son animation (légère)
    """
    xmonstre1,ymonstre1,imonstre1,monstre1,animmonstre1, viemonstre1=sous_dico['x'],sous_dico['y'],sous_dico['sens'],sous_dico['image'],sous_dico['anim'],sous_dico['vie']
    if imonstre1 == 0 :  #Si la variable de changement de sens est égale à 0 , alors :
        xmonstre1=xmonstre1+1.2  #Le monstre bouge
#Boucles pour l'animation :
        if animmonstre1 <20 :
            animmonstre1+=1
        elif animmonstre1 == 20:
            monstre1 = pygame.image.load("Images/Monstre1position5.png")
            monstre1 = pygame.transform.scale(monstre1, (52,37))
            animmonstre1+=1

        if 20 < animmonstre1 <40 :
            animmonstre1+=1
        elif animmonstre1 == 40 :
            monstre1 = pygame.image.load("Images/Monstre1position6.png")
            monstre1 = pygame.transform.scale(monstre1, (52,37))
            animmonstre1+=1

        if 40 < animmonstre1 < 60 :
            animmonstre1+=1
        elif animmonstre1 == 60 :
            monstre1 = pygame.image.load("Images/Monstre1position7.png")
            monstre1 = pygame.transform.scale(monstre1, (52,37))
            animmonstre1+=1

        if 60 < animmonstre1 < 80 :
            animmonstre1+=1
        elif animmonstre1 == 80 :
            monstre1 = pygame.image.load("Images/Monstre1position8.png")
            monstre1 = pygame.transform.scale(monstre1, (52,37))
            animmonstre1=0
#Boucle pour appeller le else de la fonction pour permettre le retour du monstre dans l'autre sens :
        if xmonstre1 >= 1149 :
            imonstre1 = 1
            animmonstre1 = 0
            monstre1 = pygame.image.load("Images/Monstre1position1.png")
            monstre1 = pygame.transform.scale(monstre1, (52,37))
    else:
##        monstre1 = pygame.image.load("Images/Monstre1position1.png")
        xmonstre1=xmonstre1-1.2
#Boucles pour l'animation :
        if animmonstre1 <20:
            animmonstre1+=1
        elif animmonstre1 == 20 :
            monstre1 = pygame.image.load("Images/Monstre1position1.png")
            monstre1 = pygame.transform.scale(monstre1, (52,37))
            animmonstre1+=1

        if 20 < animmonstre1 < 40 :
            animmonstre1+=1
        elif animmonstre1 == 40 :
            monstre1 = pygame.image.load("Images/Monstre1position2.png")
            monstre1 = pygame.transform.scale(monstre1, (52,37))
            animmonstre1+=1

        if 40 < animmonstre1 < 60 :
            animmonstre1+=1
        elif animmonstre1 == 60:
            monstre1 = pygame.image.load("Images/Monstre1position3.png")
            monstre1 = pygame.transform.scale(monstre1, (52,37))
            animmonstre1+=1

        if 60 < animmonstre1 < 80 :
            animmonstre1+=1
        elif animmonstre1 == 80 :
            monstre1 = pygame.image.load("Images/Monstre1position4.png")
            monstre1 = pygame.transform.scale(monstre1, (52,37))
            animmonstre1=0
#Boucle pour appeller le if de la fonction pour permettre le retour du monstre dans l'autre sens :
        if xmonstre1 <= 0 :
            imonstre1 = 0
            animmonstre1 = 0
            monstre1 = pygame.image.load("Images/Monstre1position5.png")
            monstre1 = pygame.transform.scale(monstre1, (52,37))

    sous_dico['x'],sous_dico['y'],sous_dico['sens'],sous_dico['image'],sous_dico['anim'],sous_dico['vie']=xmonstre1,ymonstre1,imonstre1,monstre1,animmonstre1, viemonstre1
    return sous_dico