import pygame
import random
import math
from pygame import mixer
# Abstract Factory
from abc import ABC, abstractmethod
class AbstractFactory(ABC):
    @abstractmethod
    def create_enemy(self, type):
        pass

class DevilFactory(AbstractFactory):
    def create_enemy(self, type):
        if type == 'devil': return Devil()

class GhostFactory(AbstractFactory):
    def create_enemy(self, type):
        if type == 'ghost': return Ghost()

class JokerFactory(AbstractFactory):
    def create_enemy(self, type):
        if type == 'joker': return Joker()

class VampireFactory(AbstractFactory):
    def create_enemy(self, type):
        if type == 'vampire': return Vampire()

class Enemy(ABC):
    @abstractmethod
    def enemyDisplay(self):
        pass
    @abstractmethod
    def hasCollided(self,fX,fY):
        pass

class Devil(Enemy):
    def __init__(self):
        self.enemyImg = pygame.image.load('resources/devil.png').convert()
        self.eX = random.randrange(0, 736, 10)
        self.eY = random.randrange(0, 268, 10)
        self.deX = 2
        self.deY = 3

    def enemyDisplay(self,screen):
        screen.blit(self.enemyImg, (self.eX, self.eY))

    def hasCollided(self,fX, fY):
        dist = math.sqrt(math.pow(self.eX-fX, 2) + math.pow(self.eY-fY, 2))
        if dist < 20:
            return True
        else:
            return False

    

class Ghost(Enemy):
    def __init__(self):
        self.enemyImg = pygame.image.load('resources/ghost.png').convert()
        self.eX = random.randrange(0, 736, 10)
        self.eY = random.randrange(0, 268, 10)
        self.deX = 2
        self.deY = 3

    def enemyDisplay(self,screen):
        screen.blit(self.enemyImg, (self.eX, self.eY))

    def hasCollided(self,fX, fY):
        dist = math.sqrt(math.pow(self.eX-fX, 2) + math.pow(self.eY-fY, 2))
        if dist < 20:
            return True
        else:
            return False

    
class Joker(Enemy):
    def __init__(self):
        self.enemyImg = pygame.image.load('resources/scared.png').convert()
        self.eX = random.randrange(0, 736, 10)
        self.eY = random.randrange(0, 268, 10)
        self.deX = 2
        self.deY = 3

    def enemyDisplay(self,screen):
        screen.blit(self.enemyImg, (self.eX, self.eY))

    def hasCollided(self,fX, fY):
        dist = math.sqrt(math.pow(self.eX-fX, 2) + math.pow(self.eY-fY, 2))
        if dist < 20:
            return True
        else:
            return False

    
class Vampire(Enemy):
    def __init__(self):
        self.enemyImg = pygame.image.load('resources/vampire.png').convert()
        self.eX = random.randrange(0, 736, 10)
        self.eY = random.randrange(0, 268, 10)
        self.deX = 2
        self.deY = 3

    def enemyDisplay(self,screen):
        screen.blit(self.enemyImg, (self.eX, self.eY))

    def hasCollided(self,fX, fY):
        dist = math.sqrt(math.pow(self.eX-fX, 2) + math.pow(self.eY-fY, 2))
        if dist < 20:
            collisionSound = mixer.Sound("resources/explosion.mp3")
            collisionSound.play()
            return True
        else:
            return False

    

class FactoryProducer:
    def get_factory(self, type):
        if type == 'devil': return DevilFactory()
        if type == 'ghost': return GhostFactory()
        if type == 'joker': return JokerFactory()
        if type == 'vampire': return VampireFactory()
