import pygame

from runtime import asset_path

# Initialisation de pygame
pygame.init()

# Charger la musique
pygame.mixer.music.load(asset_path("assets/Musiques/Musique_fin.mp3"))

# Lancer la musique
pygame.mixer.music.play()

# Attendre que la musique se termine
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Arrêter pygame
pygame.quit()
