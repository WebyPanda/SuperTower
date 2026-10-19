import pygame
from pygame.locals import *
pygame.init()




def gerer_fleche1(sous_dico):
    """Fonction qui prend en paramètres la position de la flèche et l'image de la flèche
    Cette fonction gère le déplacement de la flèche numéro 1

    """
    xfleche1,yfleche1,fleche1=sous_dico['x'],sous_dico['y'],sous_dico['image']
    #Boucles permettant que le x de la flèche augmente, pour la faire bouger
    if xfleche1 < 1175 :
        xfleche1=xfleche1+3
    if yfleche1 >= 225 :
        xfleche1=30
        fleche1 = pygame.image.load("Images/Flecheposition1.png").convert_alpha()
        yfleche1=190

#Boucles permettant une lègère animation de la flèche : le y augmente au fur et à mesure, la flèche descend
    if xfleche1 > 300 :
        fleche1 = pygame.image.load("Images/Flecheposition1.png").convert_alpha()
        fleche1 = pygame.transform.rotate(fleche1,-3)
        yfleche1 = yfleche1 + 0.1
    if xfleche1 > 500 :
        fleche1 = pygame.image.load("Images/Flecheposition1.png").convert_alpha()
        fleche1 = pygame.transform.rotate(fleche1,-5)
        yfleche1 = yfleche1 + 0.2
    if xfleche1 > 650 :
        fleche1 = pygame.image.load("Images/Flecheposition1.png").convert_alpha()
        fleche1 = pygame.transform.rotate(fleche1,-7)
        yfleche1 = yfleche1 + 0.3



#Boucle pour savoir si la flèche est arrivée au bout de sa course(si elle touche le bord de l'écran ou si elle touche le personnage)
#et donc pour qu'elle reparte de sa position initiale
    sous_dico['x'],sous_dico['y'],sous_dico['image']=xfleche1,yfleche1,fleche1

    return sous_dico