import pygame
class Flame(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Flame, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.flameImg = pygame.image.load('resources/flames.png')
        self.fX = 0
        self.fY = 480
        self.dfX = 2
        self.dfY = 5
        self.flameState = "ready"

    def fire_attack(self,screen,x, y):
        self.flameState = "fire"
        screen.blit(self.flameImg, (x + 16, y + 10))