import pygame

# Initialize
pygame.init()

screen = pygame.display.set_mode((800, 600))
activeStatus = True

# Loop to Game
while activeStatus:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            activeStatus = False
