import math
from player import Player
import pygame
import random
import enemy
from pygame import mixer
from flame import Flame
if __name__ == "__main__":
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
    player = Player()

    # For the enemy
    num_enemies = 1
    producer = enemy.FactoryProducer()
    enemyPlayers = []
    for i in range(0,num_enemies):
        newEnemy = random.choice(["devil","ghost","joker","vampire"])
        factory = producer.get_factory(newEnemy)
        enemyPlayer = factory.create_enemy(newEnemy)
        enemyPlayers.append(enemyPlayer)
    

    # For the flame
    flame = Flame()

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
                    player.dpY = -5
                if event.key == pygame.K_s:
                    player.dpY = 5
                if event.key == pygame.K_d:
                    player.dpX = 5
                if event.key == pygame.K_a:
                    player.dpX = -5
                if event.key == pygame.K_SPACE:
                    if flame.flameState == "ready":
                        fireSound = mixer.Sound("resources/fire.mp3")
                        fireSound.play()
                        flame.fX = player.pX
                        flame.fY = player.pY
                        flame.fire_attack(screen,flame.fX, flame.fY)
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_s):
                    player.dpY = 0
                if event.key in (pygame.K_a, pygame.K_d):
                    player.dpX = 0

        # update player coordinates
        player.pX = 736 if (player.pX + player.dpX) >= 736 else (0 if (player.pX + player.dpX) <= 0 else (player.pX + player.dpX))
        player.pY = 536 if (player.pY + player.dpY) >= 536 else (260 if (player.pY + player.dpY) <= 260 else (player.pY + player.dpY))

        #if player.playerState == "not dead":
        for i in range(0,num_enemies):
            hit = player.hasHitPlayer(enemyPlayer.eX,enemyPlayer.eY,player.pX,player.pY)
            if hit:
                enemyPlayer.eY = 2000
                player.playerState="dead"
                break

            enemyPlayers[i].eX += enemyPlayer.deX
            enemyPlayers[i].eY += enemyPlayer.deY
            if enemyPlayers[i].eX <= 0:
                enemyPlayers[i].deX = 2
            elif enemyPlayers[i].eX >= 736:
                enemyPlayers[i].deX = -2

            if enemyPlayers[i].eY <= 0:
                enemyPlayers[i].deY = 3
            elif enemyPlayers[i].eY >= 536:
                enemyPlayers[i].deY = -2


            # for Collision
            collision = enemyPlayers[i].hasCollided(flame.fX, flame.fY)
            if collision:
                enemyPlayers[i].eX = random.randrange(0, 736, 10)
                enemyPlayers[i].eY = random.randrange(0, 268, 10)
                producer = enemy.FactoryProducer()
                newEnemy = random.choice(["devil","ghost","joker","vampire"])
                factory = producer.get_factory(newEnemy)
                enemyPlayer = factory.create_enemy(newEnemy)
                enemyPlayer.eX = random.randrange(0, 736, 10)
                enemyPlayer.eY = random.randrange(0, 268, 10)
                enemyPlayers.append(enemyPlayer)
                flame.flameState = "ready"
                score_value += 1

        if (player.playerState == "dead"):
            game_over_text()
        # persist flame
        if flame.fY <= 0:
            flame.fY = 480
            flame.flameState = "ready"

        if flame.flameState == "fire":
            flame.fire_attack(screen,flame.fX, flame.fY)
            flame.fY -= flame.dfY

        player.playerDisplay(screen)
        showScore(textX, textY)
        enemyPlayer.enemyDisplay(screen)
        pygame.display.update()
