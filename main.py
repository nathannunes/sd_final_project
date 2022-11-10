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

def player():
    screen.blit(playerImg,(pX,pY))

# Loop to Game
while activeStatus:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            activeStatus = False
    # Set RGB values
    screen.fill((59, 26, 2))
    player()
    pygame.display.update()