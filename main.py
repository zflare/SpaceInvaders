import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load('SpaceInvaders\gameBackGnd.png')

# Title and Icon
pygame.display.set_caption('Kevin Space Invaders')
standShipIcon = pygame.image.load('SpaceInvaders\standShip.png')
pygame.display.set_icon(standShipIcon)

# Player
# standShip = 32x32
playerIcon = pygame.image.load('SpaceInvaders\standShip.png')
playerX = 384
playerY = 480
playerX_Movement = 0

# Enemy
# standEnemy = 48x48
enemyIcon = pygame.image.load('SpaceInvaders\standEnemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_Movement = 0.5
enemyY_Movement = 40

def player(x,y):
    screen.blit(playerIcon,(x, y))


def enemy(x,y):
    screen.blit(enemyIcon,(x, y))

# Game Loop
running = True
while running:

    # (R,G,B) color for screen max 0 - 255
    screen.fill((0,0,0))
    # Background PNG
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if key stroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_Movement = -1
                print('Left arrow')
            if event.key == pygame.K_RIGHT:
                playerX_Movement = 1
                print('Right arrow')
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Movement = 0
                print('Key released')
            else:
                print('Unknown key')

    # Player Movement
    playerX += playerX_Movement
    if playerX <= 0:
        playerX = 0
    #ship PNG=size_32 so 800-32 gives max boarder    
    elif playerX >= 768:
        playerX = 768

    # Enemy Movement
    enemyX += enemyX_Movement
    if enemyX <= 0:
        enemyX_Movement = 0.5
        enemyY += enemyY_Movement 
    elif enemyX >= 752:
        enemyX_Movement = -0.5
        enemyY += enemyY_Movement     

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()