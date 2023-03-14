# File Created By Ross Cassetta
### IMPORTS ###
import pygame as pg
import random
import os
from settings import *
from sprites import *

### ASSETS ###
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

def get_mouse_now():
    x,y = pg.mouse.get_pos()
    return (x,y)

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My first game...")
clock = pg.time.Clock() 


all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()
player = Player()

enemy1 = Mob(80,80)
enemy2 = Mob(80,80)
enemy3 = Mob(80,80)
enemy4 = Mob(80,80)


all_sprites.add(player)
all_sprites.add(enemy1)
all_sprites.add(enemy2)
all_sprites.add(enemy3)
all_sprites.add(enemy4)

# for i in range(0,20):
#     m = Mob(randint(30,90), randinti(30,90))

### GAME LOOP ###
while RUNNING:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUNNING = False
    all_sprites.update()

    blocks_hit_list = pg.sprite.spritecollide(player, enemies, True)
    for block in blocks_hit_list:
        pass
    screen.fill(BLUE)
    all_sprites.draw(screen)
    pg.display.flip()
pg.quit()