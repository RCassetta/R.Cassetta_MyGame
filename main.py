# File Created By Ross Cassetta
### IMPORTS ###
import pygame as pg
import os
from settings import *
from sprites import *

### ASSETS ###
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

def get_mouse_now():
    x,y = pg.mouse.get_pos()
    return (x,y)

# init pg and create window
pg.init()
# init sound mixer
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My first game...")
clock = pg.time.Clock() 


all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()
player = Player()

all_sprites.add(player)
player.pos = (0,0)
for i in range(0,20):
    # instantiate mobs
    m = Mob(randint.randint(30,90), randint.randint(30, 90), (RED))
    enemies.add(m)
    all_sprites.add(m)

print(enemies)
# game loop

while RUNNING:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUNNING = False
    enemies.update()
    all_sprites.update()

    blocks_hit_list = pg.sprite.spritecollide(player, enemies, False)
    for block in blocks_hit_list:
        pass
    screen.fill(BLUE)
    all_sprites.draw(screen)
    pg.display.flip()
pg.quit()