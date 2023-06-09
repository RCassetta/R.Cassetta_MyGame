import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint

vec = pg.math.Vector2

### PLAYER ###
class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
# Controls
    def input(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
        if keystate[pg.K_c]:
            self.pos.x = WIDTH/2
            self.pos.y = WIDTH/2
# Player Jump
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP
# Player Inbounds
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
            self.pos.y = 50
            self.vel.y = 0
# Player Update
    def update(self):
        self.inbounds()
        self.acc = vec(0, PLAYER_GRAV)
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

### MOBS ###
class Mob(Sprite):
    def __init__(self, game, width, height, color):
        Sprite.__init__(self)
        self.game = game
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.pos = vec(randint(0, WIDTH-self.width), randint(0, HEIGHT-self.height))
        self.vel = vec(randint(-5, 5), randint(-5, 5))
        self.acc = vec(1,1)
        self.cofric = 0.01
# Mob Inbounds
    def inbounds(self):
        if self.rect.x > WIDTH - 50 or self.rect.x < 0:
            self.vel.x *= -1
        if self.rect.y > HEIGHT - 50 or self.rect.y < 0:
            self.vel.y *= -1
# Mob Update
    def update(self):
        self.inbounds()
        self.pos += self.vel
        self.rect.center = self.pos
        target = self.game.player.pos - self.pos
        self.acc = target.normalize() * MOB_ACC
        self.vel += self.acc
        self.vel *= (1 - self.cofric)
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos

### PLATFORMS ###
class Platform(Sprite):
    def __init__(self, x, y, width, height, color, variant):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.variant = variant