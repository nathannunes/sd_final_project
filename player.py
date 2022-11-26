import pygame
import math
from pygame import mixer
class Player(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Player, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.playerImg = pygame.image.load('resources/player.png')
        self.pX = 370
        self.pY = 480
        self.dpX = 0
        self.dpY = 0
        self.playerState = "not dead"
    
    def playerDisplay(self,screen):
        screen.blit(self.playerImg, (self.pX, self.pY))

    def hasHitPlayer(self,eX, eY, pX, pY):
        dist = math.sqrt(math.pow(eX - pX, 2) + math.pow(eY - pY, 2))
        #global playerState
        self.playerState = "not dead"
        if dist < 35:
            self.playerState = "dead"
            coSound = mixer.Sound("resources/explosion.mp3")
            coSound.play()
            return True
        else:
            return False

        
