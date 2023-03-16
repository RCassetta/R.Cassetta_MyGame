import pygame as pg
import random as randint
from pygame.sprite import Sprite

from settings import *

vec = pg.math.Vector2

### PLAYER CLASS ###
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
    def input(self):
        keystate = pg.key.get_pressed()

        if keystate[pg.K_w]:
            self.acc.y = -PLAYER_ACC
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_s]:
            self.acc.y = PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
    ### BORDER ###
    def inbounds(self):
        if self.rect.x > WIDTH - 50:
            self.pos.x = WIDTH - 25
            self.vel.x = 0
        if self.rect.x < 0:
            self.pos.x = 25
            self.vel.x = 0
        if self.rect.y > HEIGHT - 50:
            self.pos.y = HEIGHT - 25
            self.vel.y = 0
        if self.rect.y < 0:
            self.pos.y = 25
            self.vel.y = 0

    def update(self):
        self.inbounds()
        self.acc = self.vel * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos
        
class Mob(Sprite):
    def __init__(self, width, height, color):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1

    def behavior(self):
        if self.rect.x > WIDTH or self.rect.x < 0:
            self.vel.x *= -1
        if self.rect.y < 0 or self.rect.y > HEIGHT:
            self.vel.y *= -1
        self.acc = vec(randint.uniform(-MOB_ACC, MOB_ACC), randint.uniform(-MOB_ACC, MOB_ACC))

    def update(self):
        self.behavior()
        self.acc = self.vel * MOB_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos

