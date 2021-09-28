import os
import sys
from random import randint, choice
from pygame.locals import *
from functions.new_aux import *

# define display surface
screen_W, screen_H = 412, 846

os.environ['SDL_VIDEO_WINDOW_POS'] = '50,50'

# game setup
pygame.init()
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((screen_W, screen_H))
pygame.display.set_caption('DEATH ROAD')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
FPS = 120

background = pygame.image.load('base_road.jpg').convert()
bg_speed = 0

# player's car
player = Player(200, 500, 10, 60, 2)

lanes = (47, 131, 222, 302)
enemies = []
bullets = []
enemy_cars = ('carro1.png', 'carro2.png', 'carro3.png', 'carro4.png', 'carro5.png')

# main loop
running = True
while running:
    rel_x = bg_speed % background.get_rect().height
    screen.blit(background, (0, rel_x - background.get_rect().height))
    if rel_x < screen_H:
        screen.blit(background, (0, rel_x))
    bg_speed += 4
    for event in pygame.event.get():
        # shoot bullet
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            bullet = Bullet('bullet.png', player.x, player.y, 4, 4, 8, x, y)
            bullets.append(bullet)
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    # player movement
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        player.moveDirection('N')
    if pressed[pygame.K_DOWN]:
        player.moveDirection('S')
    if pressed[pygame.K_LEFT]:
        player.moveDirection('W')
        player.draw('player_left.png', 23, 15)
    if pressed[pygame.K_RIGHT]:
        player.moveDirection('E')
        player.draw('player_right.png', 23, 15)
    else:
        player.draw('player_front.png', 23, 15)

    for bullet in bullets:
        bullet.move()
        bullet.draw(1, 1)
    # player limits
    if player.x <= 35:
        player.x = 35
    elif player.x >= 320:
        player.x = 320
    if player.y <= 10:
        player.y = 10
    elif player.y >= 700:
        player.y = 700

    # enemy spawn
    for enemy in enemies:
        enemy.move()
    if randint(1, 400) == 15:
        x = choice(lanes)
        enemy = Vehicle(choice(enemy_cars), x, -80, 60, 130, 5)
        enemy.direction = 'S'
        enemy.speed = 2
        enemies.append(enemy)
    for enemy in enemies:
        enemy.draw(8, 15)
    # bullet spawn
    for bullet in bullets:
        for enemy in enemies:
            if bullet.isCollision(enemy):
                enemies.remove(enemy)
                bullets.remove(bullet)

    pygame.display.update()
    CLOCK.tick(FPS)
