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

from the_ark_game import LevelOneArkGame, Seed, Comet
from the_ark_view import ArkView
from the_ark_controller import ArkController

pygame.init()
SECONDS = 60
frames_per_second = pygame.time.Clock()
game = LevelOneArkGame()
game_view = ArkView(game)

# create Sprite groups based on functionality
all_sprites = pygame.sprite.Group()
movable_sprites = pygame.sprite.Group()
# create obstacle sprites
comets = game.comets
# add the comets to all_sprites
all_sprites.add(comets)
# add the comets to movable_sprites, sprites that
# move on the screen
movable_sprites.add(comets)
# create icon sprites
seeds = game.seeds
# add the seeds to all_sprites
all_sprites.add(seeds)
player = ArkController(game, comets, seeds)
all_sprites.add(player)
movable_sprites.add(player)
display_surf = game_view.set_screen()


while True:   
    # If the player cliks the x button, the game window closes and
    # the program ends
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # redraws and updates everything on the screen, including the
    # background, sprites, and texts
    game_view.update_screen(display_surf, all_sprites, movable_sprites)
    # Allows the player to "collect" seeds and updates their score with
    # every seed they collide with
    if pygame.sprite.spritecollideany(player, seeds):
        # gets the seed the player collided with
        item = pygame.sprite.spritecollideany(player, seeds)
        # increase the score
        new_score = game.inc_score()
        # removes the collected seed from its group
        item.kill()
        # if all three seeds are collected the Win screen is displayed
        # and the game is closed shortly thereafter
        if new_score == 3:
            game_view.game_won(display_surf)
            for sprite in all_sprites:
                sprite.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()
    # Decreases the number of lives the player has when they collide
    # with a obstacle
    if pygame.sprite.spritecollideany(player, comets):
        # get the obstacle the player collided with
        enemy = pygame.sprite.spritecollideany(player, comets)
        # decrease the number of lives left
        lives_left = game.lose_life()
        # if all three lives are lost, the Loss screen is displayed
        #and the game is closed shortly thereafter
        if lives_left == 0:
            game_view.game_lost(display_surf)
            for sprite in all_sprites:
                sprite.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()
        else:
            # spawn the collided obstacle back to the top of the screen
            enemy.rect.center = (random.randint(40, game.SCREEN_WIDTH-40), 0)
    pygame.display.update()
    frames_per_second.tick(SECONDS)
