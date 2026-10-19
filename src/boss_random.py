import pygame
import random
from pygame.locals import *
pygame.init()

def deplacement_aleatoire(dico):
    x_boss, y_boss,boss, vie_boss, plusoumoins, deplacement_horizontal, total_deplacement=dico['boss']['x'],dico['boss']['y'],dico['boss']['image'],dico['boss']['vie'],dico['boss']['sens'],dico['boss']['deplacement_horizontal'],dico['boss']['total_deplacement']
##    print(x_boss, y_boss,boss, vie_boss, plusoumoins, deplacement_horizontal, total_deplacement)

    l = ["+","-"]
    if plusoumoins == "" :
        plusoumoins = random.choice(l)
        deplacement_horizontal = random.randint (50,400)
        print(deplacement_horizontal,plusoumoins)

    if deplacement_horizontal > x_boss and plusoumoins == "-" :
        deplacement_horizontal = x_boss
    elif deplacement_horizontal > 1200 - x_boss and plusoumoins == "+" :
        deplacement_horizontal = 1200 - x_boss



    # Random movement handling
##    for i in range (deplacement_horizontal):
    if plusoumoins == "+" :
        if total_deplacement < deplacement_horizontal :
            x_boss += 10
            total_deplacement += 10
        else:
            total_deplacement = 0
            plusoumoins = ""

    elif plusoumoins == "-" :
        if total_deplacement < deplacement_horizontal :
            x_boss = x_boss-10
            total_deplacement += 10
        else:
            total_deplacement = 0
            plusoumoins = ""


    # Check movement boundaries
    if x_boss < 15:
        x_boss = 15
        plusoumoins = "+"
        deplacement_horizontal=500
    if x_boss > 1134:
        x_boss = 1134
        plusoumoins = "-"
        deplacement_horizontal=500

##    print(x_boss, y_boss,boss, vie_boss, plusoumoins, deplacement_horizontal, total_deplacement)

    dico['boss']['x'],dico['boss']['y'],dico['boss']['image'],dico['boss']['vie'],dico['boss']['sens'],dico['boss']['deplacement_horizontal'],dico['boss']['total_deplacement']=x_boss,y_boss,boss, vie_boss, plusoumoins, deplacement_horizontal, total_deplacement

def boss_damage(pnj,perso):
    import pygame
    boss_rect=pygame.Rect(pnj['boss']['x'],pnj['boss']['y'],pnj['boss']['image'].get_width(),pnj['boss']['image'].get_height())
    for i, projectile in enumerate(perso['projectile_list']):
        projectile_rect=pygame.Rect(projectile[0],projectile[1],projectile[4].get_width(),projectile[4].get_height())
        if  boss_rect.colliderect(projectile_rect)==True:
            del perso['projectile_list'][i]
            # Increase the multiplier for greater difficulty
            pnj['boss']['vie']-=projectile[5]*2

