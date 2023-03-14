#This is an edit
import pygame as pg

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
###
class Mob(Sprite):
    def __init__(self,width,height):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
    # ...

    def behavior(self):
        # acc go up
        
        # self.acc.y = MOB_ACC
        # self.acc.x = MOB_ACC
        if self.rect.x > WIDTH or self.rect.x < 0 or self.rect.y < 0 or self.rect.y > HEIGHT:
            self.vel *= -1
        # if self.rect.x > WIDTH:
        #     print("I'm off the right screen...")
        # if self.rect.x < 0:
        #     print("I'm off the left screen...")
        # if self.rect.y < 0:
        #     print("I'm off the top screen...")
        #     # reduces vel
        #     self.vel *= -1
        #     self.acc *= -1
        # if self.rect.y > HEIGHT:
        #     print("I'm off the bottom screen...")

    def update(self):
        # self.inbounds()
        self.acc = self.vel * MOB_FRICTION
        self.behavior()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos