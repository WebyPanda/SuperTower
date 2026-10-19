from pygame import *
from pygame.locals import *
#Deplacement gauche droite saut
def mouvement_perso(gpc_mouvement):
    #appuyé sur la flèche haut ? et action en cours terminée ?
    if int(gpc_mouvement['touche_pressée'][K_UP])==1 and gpc_mouvement['avancement_saut']<=0 and gpc_mouvement['Touche_le_sol']==True:
        gpc_mouvement['avancement_saut']=31
        gpc_mouvement['type_action']=1
        gpc_mouvement['gravité?']=False
    #appuyé sur la flèche droite ?
    if int(gpc_mouvement['touche_pressée'][K_RIGHT])==1:
        gpc_mouvement['x']+=5
        gpc_mouvement['sens_image']=1
        #Si on touche le sol, on marche, sinonon se déplace juste sans animation
        if gpc_mouvement['Touche_le_sol']==True:
            gpc_mouvement['avancement_image']+=1
    #appuyé sur la flèche gauche ?
    elif int(gpc_mouvement['touche_pressée'][K_LEFT])==1:
        gpc_mouvement['x']-=5
        gpc_mouvement['sens_image']=0
        #Si on touche le sol, on marche, sinonon se déplace juste sans animation
        if gpc_mouvement['Touche_le_sol']==True:
            gpc_mouvement['avancement_image']+=1
    #Si on arrive à la dernière image de l'animation, on repars de la première
    if gpc_mouvement['avancement_image']>9:
        gpc_mouvement['avancement_image']=1

#Saut
#saute à 2x sa taille pied à deux fois perso
#renvoie la position en y tant que le compteur([1][1]) n'est pas à 0
def jump(gpc_saut):
        if gpc_saut['avancement_saut']>16:#le perso monte ...
            gpc_saut['y']-=10
            gpc_saut['avancement_saut']-=1
        elif gpc_saut['avancement_saut']>=0:#puis descend grace à la gravité
            gpc_saut['avancement_saut']-=1
            gpc_saut['gravité?']=True

