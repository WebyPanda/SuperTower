from runtime import asset_path
import pygame
from pygame.locals import *
from Monstre1 import gerer_monstre1
from Monstre2 import gerer_monstre2
from Monstre3 import gerer_monstre3
from Fleche1 import gerer_fleche1
from Fleche2 import gerer_fleche2

def chargement_Baptiste():
    import pygame
    dico={'monstre1':{'x':0,'y':60,'image':pygame.transform.scale(pygame.image.load(asset_path("assets/Images/Monstre1position5.png")), (52,37)),'sens':0,'anim':0,'vie':5,'réaparition_dans':0},
    'monstre2':{'x':0,'y':548,'image':pygame.transform.scale(pygame.image.load(asset_path("assets/Images/monstre 2 position 8.png")), (37,52)),'sens':0,'anim':0,'vie':5,'réaparition_dans':0},
    'monstre3':{'x':1020,'y':461,'image':pygame.transform.rotate(pygame.image.load(asset_path("assets/Images/Monstre1position5.png")),90),'sens':0,'anim':0,'vie':5,'réaparition_dans':0},
    'flèche1':{'x':30,'y':190,'image':pygame.image.load(asset_path("assets/Images/Flecheposition1.png"))},
    'flèche2':{'x':410,'y':370,'image':pygame.image.load(asset_path("assets/Images/Flecheposition1.png"))}}
    return dico

def gestion_monstres(dico,dico_perso):
    for key in dico.keys():
        if key=='monstre1':
            dico['monstre1']=gerer_monstre1(dico['monstre1'])
        if key=='monstre2':
            dico['monstre2']=gerer_monstre2(dico['monstre2'])
        if key=='monstre3':
            dico['monstre3']=gerer_monstre3(dico['monstre3'])
        if key=='flèche1':
            dico['flèche1']=gerer_fleche1(dico['flèche1'])
        if key=='flèche2':
            dico['flèche2']=gerer_fleche2(dico['flèche2'])
    monstres_damage(dico,dico_perso)
    for key in dico.keys():
        if key=='monstre1' or key=='monstre2' or key=='monstre3':
            if dico[key]['vie']<=0:
                dico[key]['vie']=5
                dico[key]['réaparition_dans']=60
    return dico

def monstres_damage(pnj,perso):
    import pygame
    monstres_rects={}
    for key in pnj.keys():
        if (key=='monstre1'  or key=='monstre2' or key=='monstre3') and pnj[key]['réaparition_dans']==0:
            monstres_rects[key]=pygame.Rect(pnj[key]['x'],pnj[key]['y'],pnj[key]['image'].get_width(),pnj[key]['image'].get_height())
    for (clé,rectangle) in monstres_rects.items():
        for i, projectile in enumerate(perso['projectile_list']):
            projectile_rect=pygame.Rect(projectile[0],projectile[1],projectile[4].get_width(),projectile[4].get_height())
            if rectangle.colliderect(projectile_rect)==True:
                del perso['projectile_list'][i]
                pnj[clé]['vie']-=projectile[5]
