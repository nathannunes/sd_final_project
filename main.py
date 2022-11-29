import math
import os
from player import Player
import pygame
import random
import enemy
from pygame import mixer
from flame import Flame


def main():
    # Initialize
    pygame.init()

    # W , H
    screen = pygame.display.set_mode((800, 600))
    activeStatus = True

    bgImage = pygame.image.load('resources/bg.png').convert()

    # bg Sound
    mixer.music.load('resources/bg-music.mp3')
    mixer.music.play(-1)

    # Game Title and Icon
    pygame.display.set_caption('A Haunting at Clemson University')
    icon = pygame.image.load('resources/ghost.png').convert()
    pygame.display.set_icon(icon)

    # For the player
    player = Player()

    # For the enemy
    producer = enemy.FactoryProducer()
    newEnemy = random.choice(["devil", "ghost", "joker", "vampire"])
    factory = producer.get_factory(newEnemy)
    enemyPlayer = factory.create_enemy(newEnemy)

    # For the flame
    flame = Flame()

    # Score count
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    textX = 10
    textY = 10

    over_font = pygame.font.Font('freesansbold.ttf', 64)
    restart_game_font = pygame.font.Font('freesansbold.ttf', 20)

    game_over = pygame.image.load('resources/game-over.png')

    def game_over_text():
        screen.blit(game_over, (290, 150))
        restart_text = restart_game_font.render("Press R to restart", True, (255, 0, 255))
        screen.blit(restart_text, (335, 400))

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
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.dpY = -5
                if event.key == pygame.K_s:
                    player.dpY = 5
                if event.key == pygame.K_d:
                    player.dpX = 5
                if event.key == pygame.K_a:
                    player.dpX = -5
                if event.key == pygame.K_r and player.playerState == "dead":
                    main()
                if event.key == pygame.K_SPACE:
                    if flame.flameState == "ready":
                        fireSound = mixer.Sound("resources/fire.mp3")
                        fireSound.play()
                        flame.fX = player.pX
                        flame.fY = player.pY
                        flame.fire_attack(screen, flame.fX, flame.fY)
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_s):
                    player.dpY = 0
                if event.key in (pygame.K_a, pygame.K_d):
                    player.dpX = 0

        # update player coordinates
        player.pX = 736 if (player.pX + player.dpX) >= 736 else (
            0 if (player.pX + player.dpX) <= 0 else (player.pX + player.dpX))
        player.pY = 536 if (player.pY + player.dpY) >= 536 else (
            260 if (player.pY + player.dpY) <= 260 else (player.pY + player.dpY))

        if player.playerState == "not dead":
            hit = player.hasHitPlayer(enemyPlayer.eX, enemyPlayer.eY, player.pX, player.pY)
            if hit:
                enemyPlayer.eY = 2000
                player.playerState = "dead"

            enemyPlayer.eX += enemyPlayer.deX
            enemyPlayer.eY += enemyPlayer.deY
            if enemyPlayer.eX <= 0:
                enemyPlayer.deX = 2
            elif enemyPlayer.eX >= 736:
                enemyPlayer.deX = -2

            if enemyPlayer.eY <= 0:
                enemyPlayer.deY = 3
            elif enemyPlayer.eY >= 536:
                enemyPlayer.deY = -2

            # for Collision
            collision = enemyPlayer.hasCollided(flame.fX, flame.fY)
            if collision:
                enemyPlayer.eX = random.randrange(0, 736, 10)
                enemyPlayer.eY = random.randrange(0, 268, 10)
                producer = enemy.FactoryProducer()
                newEnemy = random.choice(["devil", "ghost", "joker", "vampire"])
                factory = producer.get_factory(newEnemy)
                enemyPlayer = factory.create_enemy(newEnemy)
                flame.flameState = "ready"
                score_value += 1

        if (player.playerState == "dead"):
            game_over_text()
        # persist flame
        if flame.fY <= 0:
            flame.fY = 480
            flame.flameState = "ready"

        if flame.flameState == "fire":
            flame.fire_attack(screen, flame.fX, flame.fY)
            flame.fY -= flame.dfY

        player.playerDisplay(screen)
        showScore(textX, textY)
        enemyPlayer.enemyDisplay(screen)
        pygame.display.update()


if __name__ == "__main__":
    try:
        os.system('pip install pygame --upgrade')
    except:
        print("pygame upgrade not needed")
    main()
