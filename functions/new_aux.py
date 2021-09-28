import pygame, math
from random import randint

screen = pygame.display.set_mode((412, 846))


# object sizes
# car = 65, 140
# bike = 10, 60(adjust 23, 15)
# bullet = 4, 4(adjust 1, 1)

class Vehicle:
    def __init__(self, image, x, y, width, height, speed):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = 'E'
        self.speed = speed
        self.armor = 0
        self.melee = 1
        self.strength = 1
        self.life = 100

    def move(self):
        if self.direction == 'E':
            self.x = self.x + self.speed
        if self.direction == 'W':
            self.x = self.x - self.speed
        if self.direction == 'N':
            self.y = self.y - self.speed
        if self.direction == 'S':
            self.y = self.y + self.speed

    def isCollision(self, other):
        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return x_collision and y_collision

    def draw(self, x, y):
        screen.blit(self.image, (self.x - x, self.y - y))

    def set_Image(self, image: str):
        self.image = image


class Player:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = 'E'
        self.speed = speed
        self.armor = 0
        self.melee = 1
        self.strength = 1
        self.life = 100

    def moveDirection(self, direction):
        if direction == 'E':
            self.x = self.x + self.speed
        if direction == 'W':
            self.x = self.x - self.speed
        if direction == 'N':
            self.y = self.y - self.speed
        if direction == 'S':
            self.y = self.y + self.speed

    def isCollision(self, other):
        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return x_collision and y_collision

    def draw(self, image, x, y):
        screen.blit(pygame.image.load(image), (self.x - x, self.y - y))


class Bullet:
    def __init__(self, image, x, y, width, height, speed, targetx, targety):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        angle = math.atan2(targety - y, targetx - x)
        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed
        self.x = x
        self.y = y

    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.x = int(self.x)
        self.y = int(self.y)

    def isCollision(self, other):
        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return x_collision and y_collision

    def draw(self, x, y):
        screen.blit(self.image, (self.x - x, self.y - y))


