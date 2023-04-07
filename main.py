#File Created By Ross Cassetta

'''
My Goal Is:
To make the player only jump after touching the platforms // Done
Add enemy collide points to all platforms
Incorporate different types of platforms
Add health bar to player
Change enemies from blocks to animations
Change player from block to character
Add a timer and score
Add objective to game
'''


### IMPORTS ###
import pygame as pg
import os
from settings import *
from sprites import *
import tkinter as tk
from tkinter import messagebox

### ASSETS ###
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


### GAME ###
class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
        self.death_screen = False    
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        self.all_sprites.add(self.plat1)
        self.player_health = 100
        self.platforms.add(self.plat1)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(0,10):
            m = Mob(20,20,(0,255,0))
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    #Game Constants   
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    #Game Updates
    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                if hits[0].variant == "disappearing":
                    hits[0].kill()
                elif hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
        hits = pg.sprite.spritecollide(self.player, self.enemies, False)
        if hits:
            for enemy in hits:
                self.player_health -= 10
                enemy.kill()
        if self.player_health <= 0:
            self.player.kill()
            self.death_screen = True
    #Text
    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.player_health), 20, BLACK, 15,15)
        self.draw_health_bar(self.screen, 0, 0, self.player_health)
        pg.display.flip()
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    #Mouse Pos (Not Being Used)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)
    #HealthBar
    def draw_health_bar(self, surf, x, y, pct):
        if pct < 0:
            pct = 0
        BAR_LENGTH = WIDTH
        BAR_HEIGHT = 25
        fill = (pct / 100) * BAR_LENGTH
        outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
        pg.draw.rect(surf, RED, fill_rect)
        pg.draw.rect(surf, WHITE, outline_rect, 2)
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)
    def game_over(self):
        # Check if the player has died and call the death_screen function
        if self.player.health <= 0:
            self.death_screen()
    def death_screen(self):
        # Create the death screen
        window = tk.Toplevel()
        window.title("Game Over")
        label = tk.Label(window, text="You Died!")
        label.pack()
        restart_button = tk.Button(window, text="Restart Game", command=self.restart_game)
        restart_button.pack()
        exit_button = tk.Button(window, text="Exit Game", command=self.exit_game)
        exit_button.pack()


### CALLS GAME CLASS ###
g = Game()
response = messagebox.askyesno("Play Game", "Do you want to play the game?")
if response == True:
    # Start the game
        g = Game()
        g.new()
else:
    # Exit the game
        pg.quit()
    #Start New Game
while g.running:
    g.new()

pg.quit()