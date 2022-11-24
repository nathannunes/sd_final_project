import pygame
import random

# Initialize
pygame.init()

# W , H
screen = pygame.display.set_mode((800, 600))
activeStatus = True

bgImage = pygame.image.load('resources/bg.png')

# Game Title and Icon
pygame.display.set_caption('A Haunting at Clemson University')
icon = pygame.image.load('resources/ghost.png')
pygame.display.set_icon(icon)

# For the player
playerImg = pygame.image.load('resources/player.png')
pX = 370
pY = 480
dpX = 0
dpY = 0

# For the
enemyImg = pygame.image.load('resources/devil.png')
eX = random.randrange(0, 736, 10)
eY = random.randrange(0, 268, 10)
deX = 2
deY = 3

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(eX,eY):
    screen.blit(enemyImg, (eX, eY))

# Loop to Game
while activeStatus:
    # Set RGB values
    screen.fill((0, 0, 0))
    #bg image
    screen.blit(bgImage, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Tiger out")
            activeStatus = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                dpY = -2
            if event.key == pygame.K_s:
                dpY = 2
            if event.key == pygame.K_d:
                dpX = 2
            if event.key == pygame.K_a:
                dpX = -2
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                dpY = 0
            if event.key in (pygame.K_a, pygame.K_d):
                dpX = 0

    # update player coordinates
    pX = 736 if (pX + dpX) >= 736 else (0 if (pX+dpX) <= 0 else (pX+dpX))
    pY = 536 if (pY + dpY) >= 536 else (260 if (pY+dpY) <= 260 else (pY+dpY))

    eX += deX
    eY += deY
    if eX <=0:
        deX = 2
    elif eX >= 736:
        deX = -2

    if eY <=0:
        deY = 3
    elif eY >= 268:
        deY = -2

    player(pX, pY)
    enemy(eX, eY)
    pygame.display.update()