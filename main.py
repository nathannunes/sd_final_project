import math

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

# For the enemy
enemyImg = pygame.image.load('resources/devil.png')
eX = random.randrange(0, 736, 10)
eY = random.randrange(0, 268, 10)
deX = 2
deY = 3

# For the flame
flameImg = pygame.image.load('resources/flames.png')
fX = 0
fY = 480
dfX = 2
dfY = 5
flameState = "ready"

score = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(eX, eY):
    screen.blit(enemyImg, (eX, eY))


def fire_attack(x, y):
    global flameState
    flameState = "fire"
    screen.blit(flameImg, (x + 16, y + 10))


def hasCollided(eX, eY, fX, fY):
    dist = math.sqrt(math.pow(eX-fX, 2) + math.pow(eY-fY, 2))
    if dist < 20:
        return True
    else:
        return False

# Loop to Game
while activeStatus:

    # Set RGB values
    screen.fill((0, 0, 0))
    # bg image
    screen.blit(bgImage, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Tiger out")
            activeStatus = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                dpY = -5
            if event.key == pygame.K_s:
                dpY = 5
            if event.key == pygame.K_d:
                dpX = 5
            if event.key == pygame.K_a:
                dpX = -5
            if event.key == pygame.K_SPACE:
                if flameState == "ready":
                    fX = pX
                    fire_attack(fX, fY)
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                dpY = 0
            if event.key in (pygame.K_a, pygame.K_d):
                dpX = 0

    # update player coordinates
    pX = 736 if (pX + dpX) >= 736 else (0 if (pX + dpX) <= 0 else (pX + dpX))
    pY = 536 if (pY + dpY) >= 536 else (260 if (pY + dpY) <= 260 else (pY + dpY))

    eX += deX
    eY += deY
    if eX <= 0:
        deX = 2
    elif eX >= 736:
        deX = -2

    if eY <= 0:
        deY = 3
    elif eY >= 536:
        deY = -2

    # persist flame
    if fY <= 0:
        fY = 480
        flameState = "ready"

    if flameState == "fire":
        fire_attack(fX, fY)
        fY -= dfY

    # for Collision
    collision = hasCollided(eX, eY, fX, fY)
    if collision:
        eX = random.randrange(0, 736, 10)
        eY = random.randrange(0, 268, 10)
        fY = 480
        flameState = "ready"
        score += 1
        print(score)


    player(pX, pY)
    enemy(eX, eY)
    pygame.display.update()
