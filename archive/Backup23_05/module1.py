# Créé par MaisonDoucam, le 15/01/2023 en Python 3.7
# Importing the pygame module
import pygame
from pygame.locals import *
from CmdMoove import *
from FONCTIONS import *

# Initiate pygame and give permission
# to use pygame's functionality
pygame.init()

# Create a display surface object
# of specific dimension
window = pygame.display.set_mode((1200, 600))


boulle_de_neige = pygame.Surface((25, 25), pygame.SRCALPHA)
pygame.draw.circle(boulle_de_neige, (68,239,216), boulle_de_neige.get_rect().center, boulle_de_neige.get_width() // 2)

sort2_surf = pygame.Surface((15, 15), pygame.SRCALPHA)
pygame.draw.circle(sort2_surf, (249,108,26), sort2_surf.get_rect().center, sort2_surf.get_width() // 2)

sort3_surf = pygame.Surface((15, 15), pygame.SRCALPHA)
pygame.draw.circle(sort3_surf, (68,239,216), sort3_surf.get_rect().center, sort3_surf.get_width() // 2)

sort4_surf = pygame.Surface((15, 15), pygame.SRCALPHA)
pygame.draw.circle(sort4_surf, (249,108,26), sort4_surf.get_rect().center, sort4_surf.get_width() // 2)

# Create a list of different sprites
# that you want to use in the animation
image_sprite = [[[pygame.image.load("Img/hero_walking_left_1.png"),
pygame.image.load("Img/hero_walking_left_2.png"),
pygame.image.load("Img/hero_walking_left_3.png"),
pygame.image.load("Img/hero_walking_left_4.png"),
pygame.image.load("Img/hero_walking_left_5.png"),
pygame.image.load("Img/hero_walking_left_6.png"),
pygame.image.load("Img/hero_walking_left_7.png"),
pygame.image.load("Img/hero_walking_left_8.png"),
pygame.image.load("Img/hero_walking_left_9.png")],
[pygame.image.load("Img/hero_walking_right_1.png"),
pygame.image.load("Img/hero_walking_right_2.png"),
pygame.image.load("Img/hero_walking_right_3.png"),
pygame.image.load("Img/hero_walking_right_4.png"),
pygame.image.load("Img/hero_walking_right_5.png"),
pygame.image.load("Img/hero_walking_right_6.png"),
pygame.image.load("Img/hero_walking_right_7.png"),
pygame.image.load("Img/hero_walking_right_8.png"),
pygame.image.load("Img/hero_walking_right_9.png")]]]
##image_rect=image.get_rect()

# Creating a new clock object to
# track the amount of time
clock = pygame.time.Clock()

#Initializing values
x=150
y=300
image=image_sprite[0][0][0]
window.blit(image, (x, y))

#Personnage data :
dico_perso={'x':x,'y':y,'image':image,'ancienx':10,'ancieny':10,'ancienimage':0,
'touche_pressée':[0 for a in range(280)],'avancement_action':0,'saut':0,'plateformes':[(25,200,520)],
'projectile_list':[],'projectile_cooldown':0,'projectile_surfaces':[boulle_de_neige,sort2_surf,sort3_surf,sort4_surf],
'sens_image':0,'avancement_image':0,'type_action':0,'gravité?':True}
print("Contrôles :")
# Creating a boolean variable that
# we will use to run the while loop
run = True

tank_surf = pygame.Surface((1080, 120), pygame.SRCALPHA)
tank_surf.fill((0,96,0))
tank_rect = tank_surf.get_rect(midleft = (20, window.get_height() // 2))

##dico_perso=chargement_Thomas()

# Creating an infinite loop
# to run our game
while run:
	# Setting the framerate to 30fps just
	# to see the result properly
    clock.tick(60)

    #Commandes du perso
    for event in pygame.event.get():
        dico_perso['touche_pressée'] = pygame.key.get_pressed()
        for i,key in enumerate(dico_perso['touche_pressée']):
            if key==1:
                print(i)
        if event.type == QUIT:
             run = False
    x,y,image,dico_perso=gestion_personnage(dico_perso,image_sprite)

	# Displaying the image in our game window
    window.blit(tank_surf, (0,600))
    for bullet_pos in dico_perso['projectile_list']:
        window.blit(bullet_pos[4], bullet_pos[4].get_rect(center = (bullet_pos[0],bullet_pos[1])))
    window.blit(image, (x, y))

	# Updating the display surface
    pygame.display.update()

	# Filling the window with black color
    window.fill((0, 0, 0))
pygame.quit()
exit()