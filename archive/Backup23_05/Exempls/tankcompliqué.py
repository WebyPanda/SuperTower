import pygame

pygame.init()

# ======================= Variables =======================

# ------------------------ Screen -------------------------

screenWidth = 1060
screenHeight = 798
screenSize = (screenWidth, screenHeight)
display = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Tank game")



# ------------------------ Player -------------------------


# ------------------------ Enemy -------------------------


# ----------------------- Other ---------------------------

red = (155, 0, 0)

clock = pygame.time.Clock()
fps = 60


# ========================= Clases ========================


class player(pygame.sprite.Sprite):
    def __init__(self, location, angle, vel, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/player/player_tank.png")

        self.x = x
        self.y = y
        self.vel = vel
        self.angle = angle
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

        if self.angle == 360:
            self.angle = 0

    def rotate(self):
        rot_image = pygame.transform.rotate(self.image, self.angle)
        rot_rect = rot_image.get_rect(center=self.rect.center)
        return rot_image, rot_rect

    def moving_after_angle_change(self):
        x = round(math.cos(math.radians(self.angle + 90)), 1) * self.vel
        y = round(math.sin(math.radians(self.angle - 90)), 1) * self.vel
        return x, y


class enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, end):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/enemy/enemy_tank.png")

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.y, self.end]
        self.vel = 5

    def draw(self, display):
        self.move()
        display.blit(self.image, (self.x, self.y))

    def move(self):
        if self.vel > 0:
            pass


# Bullet
bullet = pygame.image.load("sprites/bullet/bullet.png")
bullet = pygame.transform.scale(bullet, (16, 16))
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 10
bullet_state = 'ready'


# ======================= Functions =======================

def redrawGameWindow():
    display.blit(bg, (0, 0))
    display.blit(player_tank.image, player_tank.rect)
    display.blit(enemy_tank.image, (enemy_tank.x, enemy_tank.y))
    #display.blit(bullet, (player_tank.x + 160, player_tank.y + 100))

    pygame.display.flip()


def fireBullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    display.blit(bullet, (x + 16, y + 10))


player_location = [70, 570]
player_angle = 270
player_angle_change = 0
player_vel = 0
player_x_change = 0
player_y_change = 0
player_tank_x_change_store = 0
player_tank_y_change_store = 0

run = True

while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_vel = 2
            elif event.key == pygame.K_DOWN:
                player_vel = -2
            elif event.key == pygame.K_LEFT:
                player_angle_change = 2
            elif event.key == pygame.K_RIGHT:
                player_angle_change = -2

            if event.key == pygame.K_SPACE:
                display.blit(bullet, (player_tank.x + 160, player_tank.y + 100))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_vel = 0
            elif event.key == pygame.K_DOWN:
                player_vel = 0
            elif event.key == pygame.K_LEFT:
                player_angle_change = 0
            elif event.key == pygame.K_RIGHT:
                player_angle_change = 0

    player_angle += player_angle_change

    player_tank = player(player_location, player_angle, player_vel, player_x_change, player_y_change)

    enemy_tank = enemy(800, 170, 64, 64, 700)

    player_tank.image, player_tank.rect = player_tank.rotate()

    player_tank.x_change, player_tank.y_change = player_tank.moving_after_angle_change()

    player_tank_x_change_store += player_tank.x_change
    player_tank_y_change_store += player_tank.y_change
    player_tank.rect.centerx += player_tank_x_change_store
    player_tank.rect.centery += player_tank_y_change_store

    # Bullet movement
    if bullet_state == "fire":
        fireBullet(player_tank.x, bullet_y)
        bullet_y -= bullet_y_change

    redrawGameWindow()

pygame.quit()
quit()