import pygame
from pygame import mixer
import random
import math

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load('SpaceInvaders\gameBackGnd.png')

# Background Sound
mixer.music.load('SpaceInvaders\8BIT_Crossing_Field _LiSA_FULL.ogg')
mixer.music.play(-1)

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
enemyIcon = []
enemyX = []
enemyY = []
enemyX_Movement = []
enemyY_Movement = []
numOfEnemies = 6

for i in range(numOfEnemies):
    enemyIcon.append(pygame.image.load('SpaceInvaders\standEnemy.png'))
    enemyX.append(random.randint(0, 755))
    enemyY.append(random.randint(50, 150))
    enemyX_Movement.append(0.5)    
    enemyY_Movement.append(40)

# Bullet
# standBullet = 32x32
# Ready = bullet waiting to launch
# Fire = bullet moving in Y axis
bulletIcon = pygame.image.load('SpaceInvaders\standBullet.png')
bulletX = 0
bulletY = 480
bulletX_Movement = 0
bulletY_Movement = 2
bullet_state = 'Ready'

# Score
scoreValue = 0
scoreFont = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

# Game Over Text
gameOverFont = pygame.font.Font('freesansbold.ttf',64)



def scoreDisplayed(x,y):
    score = scoreFont.render('Score : ' + str(scoreValue), True, (225,225,225))
    screen.blit(score,(x, y))


def gameOverText():
    overText = gameOverFont.render('GAME OVER', True, (225,225,225))
    screen.blit(overText,(200, 250))

def player(x,y):
    screen.blit(playerIcon,(x, y))


def enemy(x,y,i):
    screen.blit(enemyIcon[i],(x, y))


def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'Fire'
    screen.blit(bulletIcon, (x, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    dxValue = math.pow((enemyX - bulletX),2)
    dyValue = math.pow((enemyY - bulletY),2)
    distance = math.sqrt((dxValue + dyValue))
    if distance < 27:
        return True
    else:
        return False

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
                #print('Left arrow')
            if event.key == pygame.K_RIGHT:
                playerX_Movement = 1
                #print('Right arrow')
            if event.key == pygame.K_SPACE:
                if bullet_state == 'Ready':
                    bulletSound = mixer.Sound('SpaceInvaders\laser.wav')
                    bulletSound.play()
                    # gets current x cord of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    #print('Space Key')   
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Movement = 0
                #print('Key released')
            #else:
                #print('Unknown key')

    # Player Movement
    playerX += playerX_Movement
    if playerX <= 0:
        playerX = 0
    
    #ship PNG=size_32 so 800-32 gives max boarder    
    elif playerX >= 768:
        playerX = 768

    # Enemy Movement
    for i in range(numOfEnemies):
        # Game Over
        if enemyY[i] > 440:
            for j in range(numOfEnemies):
                enemyY[j] = 2000
            gameOverText()
            break

        enemyX[i] += enemyX_Movement[i]
        if enemyX[i] <= 0:
            enemyX_Movement[i] = 0.5
            enemyY[i] += enemyY_Movement[i] 
        elif enemyX[i] >= 752:
            enemyX_Movement[i] = -0.5
            enemyY[i] += enemyY_Movement[i]
    # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound('SpaceInvaders\explosion.wav')
            explosionSound.play()
            bulletY = 480
            bullet_state = 'Ready'
            scoreValue += 1
            #print(scoreValue)
            enemyX[i] = random.randint(0, 755)
            enemyY[i] = random.randint(50, 150)
        
        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'Ready'
    if bullet_state == 'Fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_Movement

    player(playerX, playerY)
    scoreDisplayed(textX,textY)
    pygame.display.update()