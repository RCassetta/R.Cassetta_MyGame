# # File Created By Ross Cassetta
# ### IMPORTS ###
# import pygame as pg
# import os
# from settings import *
# from sprites import *
# from random import randint

# ### ASSETS ###
# game_folder = os.path.dirname(__file__)
# img_folder = os.path.join(game_folder, "img")

# def get_mouse_now():
#     x,y = pg.mouse.get_pos()
#     return (x,y)

# # init pg and create window
# pg.init()
# # init sound mixer
# pg.mixer.init()
# screen = pg.display.set_mode((WIDTH, HEIGHT))
# pg.display.set_caption("My first game...")
# clock = pg.time.Clock() 


# all_sprites = pg.sprite.Group()
# enemies = pg.sprite.Group()
# player = Player()
# mob1 = Mob(10,10, RED)
# all_sprites.add(player)
# player.pos = (0,0)

# print(enemies)
# # game loop

# while RUNNING:
#     clock.tick(FPS)
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             RUNNING = False
#     enemies.update()
#     all_sprites.update()

#     blocks_hit_list = pg.sprite.spritecollide(player, enemies, False)
#     for block in blocks_hit_list:
#         pass
#     screen.fill(BLUE)
#     all_sprites.draw(screen)
#     pg.display.flip()
# pg.quit()











# # File Created By Ross Cassetta

# ### IMPORTS ###
import pygame as pg
import os
from settings import *
from sprites import *
from random import randint

# ### ASSETS ###
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

### SCORE ###
def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

def get_mouse_now():
    x,y = pg.mouse.get_pos()
    return (x,y)

### SCREEN ###
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My first game...")
clock = pg.time.Clock() 

### SPRITES ###
all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()

player = Player()

all_sprites.add(player)
player.pos = (0,0)

### MOBS ###
for i in range(0,20):
    # instantiate mobs
    m = Mob(randint(30,90), randint(30, 90), (255,0,0))
    # add enemies to enemies and all_sprites...
    enemies.add(m)
    all_sprites.add(m)
print(enemies)

### GAME ###
while RUNNING:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUNNING = False
    enemies.update()
    all_sprites.update()
    ### COLLISION ###
    blocks_hit_list = pg.sprite.spritecollide(player, enemies, True)
    
    if blocks_hit_list:
        SCORE += 1

    for block in blocks_hit_list:
        print(block)
        pass
    
    screen.fill(BLUE)
    all_sprites.draw(screen)
    draw_text("Score: " + str(SCORE), 22, WHITE, WIDTH/2, HEIGHT/10)
    pg.display.flip()
pg.quit()