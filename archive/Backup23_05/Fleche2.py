import pygame
from pygame.locals import *
pygame.init()





def gerer_fleche2(sous_dico):
    """Fonction qui prend en paramètres la position de la flèche et l'image de la flèche
    Cette fonction gère le déplacement de la flèche numéro 2
    """
    xfleche2,yfleche2,fleche2=sous_dico['x'],sous_dico['y'],sous_dico['image']
    if xfleche2 < 1175 :
        xfleche2=xfleche2+3

#Boucle pour savoir si la flèche est arrivée au bout de sa course(si elle touche le bord d'un bloc)
#et donc pour qu'elle reparte de sa position initiale

    if yfleche2 >= 410 :
        xfleche2=410
        fleche2 = pygame.image.load("Images/Flecheposition1.png").convert_alpha()
        yfleche2=370

#Boucles permettant une lègère animation de la flèche : le y augmente au fur et à mesure, la flèche descend
    if xfleche2 > 500 :
        fleche2 = pygame.image.load("Images/Flecheposition1.png").convert_alpha()
        fleche2 = pygame.transform.rotate(fleche2,-3)
        yfleche2 = yfleche2 + 0.1
    if xfleche2 > 640 :
        fleche2 = pygame.image.load("Images/Flecheposition1.png").convert_alpha()
        fleche2 = pygame.transform.rotate(fleche2,-5)
        yfleche2 = yfleche2 + 0.2
    if xfleche2 > 730 :
        fleche2 = pygame.image.load("Images/Flecheposition1.png").convert_alpha()
        fleche2 = pygame.transform.rotate(fleche2,-8)
        yfleche2 = yfleche2 + 0.3

    sous_dico['x'],sous_dico['y'],sous_dico['image']=xfleche2,yfleche2,fleche2
    return  sous_dico


##or (xfleche2==xmonstre1 and yfleche2 == ymonstre1) or (xfleche2==xmonstre2 and yfleche2 == ymonstre2) or (xfleche2==xmonstre3 and yfleche2 == ymonstre3):