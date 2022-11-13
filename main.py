import pygame

# Initialize
pygame.init()

# W , H
screen = pygame.display.set_mode((800, 600))
activeStatus = True

# Game Title and Icon
pygame.display.set_caption('The Haunting at Clemson University')
icon = pygame.image.load('resources/ghost.png')
pygame.display.set_icon(icon)

# For the player
playerImg = pygame.image.load('resources/player.png')
pX = 370
pY = 480
dpX = 0
dpY = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

# Loop to Game
while activeStatus:
    # Set RGB values
    #screen.fill((59, 26, 2))
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Tiger out")
            activeStatus = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.button)

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
                dpX =0

    # update player coordinates
    pX = 736 if (pX + dpX) >= 736 else (0 if (pX+dpX)<=0 else (pX+dpX))
    pY = 536 if (pY + dpY) >= 536 else (0 if (pY+dpY)<=0 else (pY+dpY))
    player(pX,pY)
    pygame.display.update()