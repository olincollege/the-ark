# function that ties the Model-View_controller classes together
import pygame, sys
from pygame.locals import *
import random, time

from the_ark_game import *
from the_ark_view import *
from the_ark_controller import *

def main():
    pygame.init()
    
    FPS = 60
    FramePerSec = pygame.time.Clock()
    
    
    game = ArkGame()
    game_view = ArkView(game)
    

    
    all_sprites = pygame.sprite.Group()
    movable_sprites = pygame.sprite.Group()
    
    comets = pygame.sprite.Group(Comet(game,2), Comet(game,3), Comet(game,4))
    all_sprites.add(comets)
    movable_sprites.add(comets)
    
    seed_img = "carrot.png"
    seeds = pygame.sprite.Group(Seed(game, seed_img, 200, 400), 
                                Seed(game, seed_img, 500, 250),
                                Seed(game, seed_img, 250, 100))
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
        FramePerSec.tick(FPS)

if __name__ == "__main__":
    main()
