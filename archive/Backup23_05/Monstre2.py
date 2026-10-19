import pygame
from pygame.locals import *
pygame.init()



def gerer_monstre2(sous_dico):

    """
    Fonction qui prend en paramètres la position du monstre, la variable de changement de sens , l'image du monstre, la variable d'animation, le rectangle du monstre, et la vie du monstre
    Cette fonction gère le déplacement du monstre, si il doit aller vers la droite, la gauche, et son animation (légère)
    """
    xmonstre2,ymonstre2,imonstre2,monstre2,animmonstre2,viemonstre2=sous_dico['x'],sous_dico['y'],sous_dico['sens'],sous_dico['image'],sous_dico['anim'],sous_dico['vie']
    if imonstre2 == 0 :  #Si la variable de changement de sens est égale à 0 , alors :
        xmonstre2=xmonstre2+0.8  #Le monstre bouge
#Boucles pour l'animation :
        if animmonstre2 <20 :
            animmonstre2+=1
        elif animmonstre2 == 20:
            monstre2 = pygame.image.load("Images/monstre 2 position 8.png")
            monstre2 = pygame.transform.scale(monstre2, (37,52))
            animmonstre2+=1

        if 20 < animmonstre2 <40 :
            animmonstre2+=1
        elif animmonstre2 == 40 :
            monstre2 = pygame.image.load("Images/monstre 2 position 9.png")
            monstre2 = pygame.transform.scale(monstre2, (37,52))
            animmonstre2+=1

        if 40 < animmonstre2 < 60 :
            animmonstre2+=1
        elif animmonstre2 == 60 :
            monstre2 = pygame.image.load("Images/monstre 2 position 10.png")
            monstre2 = pygame.transform.scale(monstre2, (37,52))
            animmonstre2+=1

        if 60 < animmonstre2 < 80 :
            animmonstre2+=1
        elif animmonstre2 == 80 :
            monstre2 = pygame.image.load("Images/monstre 2 position 11.png")
            monstre2 = pygame.transform.scale(monstre2, (37,52))
            animmonstre2+=1
        if 80 < animmonstre2 < 100 :
            animmonstre2+=1
        elif animmonstre2 == 100 :
            monstre2 = pygame.image.load("Images/monstre 2 position 12.png")
            monstre2 = pygame.transform.scale(monstre2, (37,52))
            animmonstre2+=1

        if 100 < animmonstre2 < 120 :
            animmonstre2+=1
        elif animmonstre2 == 120 :
            monstre2 = pygame.image.load("Images/monstre 2 position 13.png")
            monstre2 = pygame.transform.scale(monstre2, (37,52))
            animmonstre2+=1

        if 120 < animmonstre2 < 140 :
            animmonstre2+=1
        elif animmonstre2 == 140 :
            monstre2 = pygame.image.load("Images/monstre 2 position 14.png")
            monstre2 = pygame.transform.scale(monstre2, (37,52))
            animmonstre2=0

#Boucle pour appeller le else de la fonction pour permettre le retour du monstre dans l'autre sens :
        if xmonstre2 >= 659 :
            imonstre2 = 1
            animmonstre2 = 0
            monstre2 = pygame.image.load("Images/monstre 2 position 1.png")
            monstre2 = pygame.transform.scale(monstre2, (37,52))

##Gère le retour du monstre avec son animation:
    else:

        xmonstre2=xmonstre2-0.8
#Boucles pour l'animation :
        if animmonstre2 <20 :
            animmonstre2+=1
        elif animmonstre2 == 20:
            monstre2 = pygame.image.load("Images/monstre 2 position 1.png")
            monstre2 = pygame.transform.scale(monstre2, (37,52))
            animmonstre2+=1

        if 20 < animmonstre2 <40 :
            animmonstre2+=1
        elif animmonstre2 == 40 :
            monstre2 = pygame.image.load("Images/monstre 2 position 2.png")
            monstre2 = pygame.transform.scale(monstre2, (37,52))
            animmonstre2+=1

        if 40 < animmonstre2 < 60 :
            animmonstre2+=1
        elif animmonstre2 == 60 :
            monstre2 = pygame.image.load("Images/monstre 2 position 3.png")
            monstre2 = pygame.transform.scale(monstre2, (37,52))
            animmonstre2+=1

        if 60 < animmonstre2 < 80 :
            animmonstre2+=1
        elif animmonstre2 == 80 :
            monstre2 = pygame.image.load("Images/monstre 2 position 4.png")
            monstre2 = pygame.transform.scale(monstre2, (37,52))
            animmonstre2+=1

        if 80 < animmonstre2 < 100 :
            animmonstre2+=1
        elif animmonstre2 == 100 :
            monstre2 = pygame.image.load("Images/monstre 2 position 5.png")
            monstre2 = pygame.transform.scale(monstre2, (37,52))
            animmonstre2+=1

        if 100 < animmonstre2 < 120 :
            animmonstre2+=1
        elif animmonstre2 == 120 :
            monstre2 = pygame.image.load("Images/monstre 2 position 6.png")
            monstre2 = pygame.transform.scale(monstre2, (37,52))
            animmonstre2+=1

        if 120 < animmonstre2 < 140 :
            animmonstre2+=1
        elif animmonstre2 == 140 :
            monstre2 = pygame.image.load("Images/monstre 2 position 7.png")
            monstre2 = pygame.transform.scale(monstre2, (37,52))
            animmonstre2=0

#Boucle pour appeller le if de la fonction pour permettre le retour du monstre dans l'autre sens :

        if xmonstre2 <= 5 :
            imonstre2 = 0
            animmonstre2 = 0
            monstre2 = pygame.image.load("Images/monstre 2 position 8.png")
            monstre2 = pygame.transform.scale(monstre2, (52,37))

    sous_dico['x'],sous_dico['y'],sous_dico['sens'],sous_dico['image'],sous_dico['anim'],sous_dico['vie']=xmonstre2,ymonstre2,imonstre2,monstre2,animmonstre2,viemonstre2
    return sous_dico




