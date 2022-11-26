import math

import pygame
import random
from pygame import mixer

# Initialize
pygame.init()

# W , H
screen = pygame.display.set_mode((800, 600))
activeStatus = True

bgImage = pygame.image.load('resources/bg.png')

# bg Sound
mixer.music.load('resources/bg-music.mp3')
mixer.music.play(-1)

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
enemyImg = []
eX = []
eY = []
deX = []
deY = []

# change for difficulty
num_of_enemies = 1

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('resources/devil.png'))
    eX.append(random.randrange(0, 736, 10))
    eY.append(random.randrange(0, 268, 10))
    deX.append(2)
    deY.append(3)

# For the flame
flameImg = pygame.image.load('resources/flames.png')
fX = 0
fY = 480
dfX = 2
dfY = 5
flameState = "ready"

# Score count
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

game_over = pygame.image.load('resources/game-over.png')


def game_over_text():
    screen.blit(game_over, (290, 150))


def showScore(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 0, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(eX, eY, i):
    screen.blit(enemyImg[i], (eX, eY))


def fire_attack(x, y):
    global flameState
    flameState = "fire"
    screen.blit(flameImg, (x + 16, y + 10))


def hasCollided(eX, eY, fX, fY):
    dist = math.sqrt(math.pow(eX - fX, 2) + math.pow(eY - fY, 2))
    if dist < 20:
        collisionSound = mixer.Sound("resources/explosion.mp3")
        collisionSound.play()
        return True
    else:
        return False


def hasHitPlayer(eX, eY, pX, pY):
    dist = math.sqrt(math.pow(eX - pX, 2) + math.pow(eY - pY, 2))
    global playerState
    playerState = "not dead"
    if dist < 35:
        playerState = "dead"
        coSound = mixer.Sound("resources/explosion.mp3")
        coSound.play()
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
                    fireSound = mixer.Sound("resources/fire.mp3")
                    fireSound.play()
                    fX = pX
                    fY = pY
                    fire_attack(fX, fY)
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                dpY = 0
            if event.key in (pygame.K_a, pygame.K_d):
                dpX = 0

    # update player coordinates
    pX = 736 if (pX + dpX) >= 736 else (0 if (pX + dpX) <= 0 else (pX + dpX))
    pY = 536 if (pY + dpY) >= 536 else (260 if (pY + dpY) <= 260 else (pY + dpY))

    for i in range(num_of_enemies):
        # Game Over
        hit = hasHitPlayer(eX[i], eY[i], pX, pY)
        if hit or eY[i] > 1000:
            for j in range(num_of_enemies):
                eY[j] = 2000
            playerState = 'dead'
            break

        eX[i] += deX[i]
        eY[i] += deY[i]
        if eX[i] <= 0:
            deX[i] = 2
        elif eX[i] >= 736:
            deX[i] = -2

        if eY[i] <= 0:
            deY[i] = 3
        elif eY[i] >= 536:
            deY[i] = -2

        # for Collision
        collision = hasCollided(eX[i], eY[i], fX, fY)
        if collision:
            eX[i] = random.randrange(0, 736, 10)
            eY[i] = random.randrange(0, 268, 10)
            fY = pY
            flameState = "ready"
            score_value += 1

        enemy(eX[i], eY[i], i)

    if (playerState == "dead"):
        game_over_text()

    # persist flame
    if fY <= 0:
        fY = 480
        flameState = "ready"

    if flameState == "fire":
        fire_attack(fX, fY)
        fY -= dfY

    player(pX, pY)
    showScore(textX, textY)
    pygame.display.update()
