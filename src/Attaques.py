# Docstrings, OK
from pygame import *
from pygame.locals import *

#Quand la touche d'un sort a été préssé
def sort(gpc_sort):
    #Si le dernier projectile lancé était il y a assez longtemps
    if gpc_sort['projectile_cooldown']==0:
        #Identification du sort en fonction de la touche préssée
        if gpc_sort['touche_pressée'][97]==1:
            #'projectible_list'.append((x,y,type de projectile,direction,avancement du projectile,son image,dégats causés par lui))
            gpc_sort['projectile_list'].append((gpc_sort['x']+20,gpc_sort['y']+40,gpc_sort['sens_image'],50,gpc_sort['projectile_surfaces'][0],5))
            #Mise à jour du temps avant prochain projectile
            gpc_sort['projectile_cooldown']=60
        if gpc_sort['touche_pressée'][115]==1:
            gpc_sort['projectile_list'].append((gpc_sort['x']+20,gpc_sort['y']+25,gpc_sort['sens_image'],0.1,gpc_sort['projectile_surfaces'][1][gpc_sort['sens_image']],2))
            gpc_sort['projectile_cooldown']=30
        if gpc_sort['touche_pressée'][120]==1:
            gpc_sort['projectile_list'].append((gpc_sort['x']+20,gpc_sort['y']+25,gpc_sort['sens_image'],0.1,gpc_sort['projectile_surfaces'][2][gpc_sort['sens_image']],3))
            gpc_sort['projectile_cooldown']=45

#Gestion des sort une fois lancés
def gestion_sort(gpc_g_s):
    #On prend le truple associé à chaque projectile présent ainsi que sa position dans la liste
    for i, bullet_pos in enumerate(gpc_g_s['projectile_list']):
        #Identifiaction du sort en focntion de son image
        if bullet_pos[4]==gpc_g_s['projectile_surfaces'][0]:
            #lancement du programme spécifique au sort
            boulle_de_neige(bullet_pos,gpc_g_s,i)
        if bullet_pos[4]==gpc_g_s['projectile_surfaces'][1][0] or bullet_pos[4]==gpc_g_s['projectile_surfaces'][1][1]:
            arrow(bullet_pos,gpc_g_s,i)
        if bullet_pos[4]==gpc_g_s['projectile_surfaces'][2][0] or bullet_pos[4]==gpc_g_s['projectile_surfaces'][2][1]:
            boulle_de_feu(bullet_pos,gpc_g_s,i)

def boulle_de_neige(boulle,gpc_bdn,i):
    #création d'une petite liste à la place du tuple pour pouvoir le modifier
    minitab=[gpc_bdn['projectile_list'][i][0],gpc_bdn['projectile_list'][i][1],gpc_bdn['projectile_list'][i][2],gpc_bdn['projectile_list'][i][3],gpc_bdn['projectile_list'][i][4]]
    #avancer à droite ou gauche en fonction de la direction du projectile
    if minitab[2]==1:
        minitab[0]+=10
    else:
        minitab[0]-=10
    #Baisse de l'avancement de la boulle (jusqu'à ce qu'elle disparaisse)
    minitab[3]-=1
    #Chute de la boulle si elle n'est pas au sol
    if minitab[1]<590:
        minitab[1]+=10
    #replacement à la hauteur du sol si à cause d'un bug la boulle est en dessous du sol
    if minitab[1]>585:
        minitab[1]=590
    #Remplacement du tuple à sa place après modification
    gpc_bdn['projectile_list'][i]=minitab[0],minitab[1],minitab[2],minitab[3],minitab[4],5
    #Supression de la boulle de neige si l'avancement atteint 0 et qu'elle doit disparaitre
    if gpc_bdn['projectile_list'][i][3] <=0 :
        del gpc_bdn['projectile_list'][i]

def arrow(flèche,gpc_arrow,i):
    #avancer à droite ou gauche en fonction de la direction du projectile
    if flèche[2]==1:
        #remplacement du tuple avec l'abscisse qui avance, la hauteur qui baisse de x pixels et x qui augmente (provoquant un effet de gravité)
        gpc_arrow['projectile_list'][i]=flèche[0]+10, flèche[1]+flèche[3],flèche[2],flèche[3]*1.07,flèche[4],2
    else:
        gpc_arrow['projectile_list'][i]=flèche[0]-10, flèche[1]+flèche[3],flèche[2],flèche[3]*1.07,flèche[4],2
    #si la flèche touche le sol, elle disaparait
    if flèche[1] > 585:
        del gpc_arrow['projectile_list'][i]

#Meme fonctionnement que la flèche
def boulle_de_feu(feu,gpc_bdf,i):
    if feu[2]==1:
        gpc_bdf['projectile_list'][i]=feu[0]+10, feu[1]+feu[3],feu[2],feu[3]*1.07,feu[4],3
    else:
        gpc_bdf['projectile_list'][i]=feu[0]-10, feu[1]+feu[3],feu[2],feu[3]*1.07,feu[4],3
    if feu[1] > 585:
        del gpc_bdf['projectile_list'][i]

