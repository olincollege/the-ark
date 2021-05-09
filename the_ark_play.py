"""
The main function that manages the ArkGame (Model),
ArkView (View), and ArkController (Controller) classes of
The Ark.
"""
import sys
import time
import random
import pygame
from pygame.locals import QUIT

from the_ark_game import LevelOneArkGame
from the_ark_view import ArkView
from the_ark_controller import ArkController

pygame.init()
SECONDS = 60
frames_per_second = pygame.time.Clock()
game = LevelOneArkGame()
game_view = ArkView(game)

all_sprites = pygame.sprite.Group()
movable_sprites = pygame.sprite.Group()
comets = LevelOneArkGame.generate_obstacles(game)
all_sprites.add(comets)
movable_sprites.add(comets)
seeds = game.generate_seeds()
all_sprites.add(seeds)
player = ArkController(game, comets, seeds)
all_sprites.add(player)
movable_sprites.add(player)
DISPLAYSURF = game_view.set_screen()


while True:     
    for event in pygame.event.get():             
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # redraws and updates everything on the screen, including the
    # background, sprites, and texts
    game_view.update_screen(DISPLAYSURF, all_sprites, movable_sprites)
    
    if pygame.sprite.spritecollideany(player, seeds):
        item = pygame.sprite.spritecollideany(player, seeds)
        new_score = game.inc_score()
        item.kill()
        if new_score == 3:
            game_view.game_won(DISPLAYSURF)
            for sprite in all_sprites:
                sprite.kill() 
            time.sleep(2)
            pygame.quit()
            sys.exit()
            
    if pygame.sprite.spritecollideany(player, comets):
        enemy = pygame.sprite.spritecollideany(player, comets)
        lives_left = game.lose_life()
        if lives_left == 0:    
            game_view.game_lost(DISPLAYSURF)
            for sprite in all_sprites:
                sprite.kill() 
            time.sleep(2)
            pygame.quit()
            sys.exit()
        else:
            enemy.rect.center = (random.randint(40, game.SCREEN_WIDTH-40), 0)
          
    pygame.display.update()
    frames_per_second.tick(SECONDS)

