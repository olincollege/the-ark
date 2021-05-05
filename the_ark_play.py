# function that ties the Model-View_controller classes together
import pygame, sys
from pygame.locals import *
import random, time

from the_ark_view import *
from the_ark_game import *
from the_ark_controller import *

def main():
    pygame.init()
    
    FPS = 60
    FramePerSec = pygame.time.Clock()
    
    
    game = ArkGame()
    game_view = ArkView(game)
    
    #Setting up Fonts
    font = pygame.font.SysFont("Verdana", 60)
    font_small = pygame.font.SysFont("Verdana", 20)
    game_over = font.render("Game Over", True, game.BLACK)
    game_won = font.render("You won!", True, game.BLACK)
    
    all_sprites = pygame.sprite.Group()
    movable_sprites = pygame.sprite.Group()
    
    comets = pygame.sprite.Group(Comet(game,4), Comet(game,5), Comet(game,6))
    all_sprites.add(comets)
    movable_sprites.add(comets)
    
    seed_img = "carrot.png"
    seeds = pygame.sprite.Group(Seed(game, seed_img), Seed(game, seed_img),
                                Seed(game, seed_img))
    all_sprites.add(seeds)
    
    player = ArkController(game, comets, seeds) 
    all_sprites.add(player)
    movable_sprites.add(player)
    
    
    
    #this block of code can be a View class method that starts the screen
    DISPLAYSURF = pygame.display.set_mode((game.SCREEN_WIDTH, game.SCREEN_HEIGHT))
    DISPLAYSURF.fill(game.WHITE)
    pygame.display.set_caption("Game")
    
    
    while True:     
        for event in pygame.event.get():              
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        # this block of code could be an "update_view" method that paint the screen
        # white and redraw the player; this is definitely a View method
        DISPLAYSURF.blit(game.background, (0,0))
        scores = font_small.render(f"SCORE: {game.score}", True, game.WHITE)
        DISPLAYSURF.blit(scores, (game.SCREEN_WIDTH-100,10)) 
        life = font_small.render(f"LIVES: {game.lives}", True, game.WHITE)
        DISPLAYSURF.blit(life, (game.SCREEN_WIDTH-100,30))
        
        for sprite in all_sprites:
            DISPLAYSURF.blit(sprite.image, sprite.rect)
            if sprite in movable_sprites:
                sprite.move()
        
        if pygame.sprite.spritecollideany(player, seeds):
            item = pygame.sprite.spritecollideany(player, seeds)
            new_score = game.inc_score()
            item.kill()
            if new_score == 3:
                DISPLAYSURF.fill(game.BLUE)
                DISPLAYSURF.blit(game_won, (game.SCREEN_WIDTH/2, game.SCREEN_HEIGHT/2)) 
                pygame.display.update()
                for sprite in all_sprites:
                    sprite.kill() 
                time.sleep(2)
                pygame.quit()
                sys.exit()
               
        if pygame.sprite.spritecollideany(player, comets):
            enemy = pygame.sprite.spritecollideany(player, comets)
            lives_left = game.lose_life()
            if lives_left == 0:    
                DISPLAYSURF.fill(game.RED)
                DISPLAYSURF.blit(game_over, (game.SCREEN_WIDTH/2, game.SCREEN_HEIGHT/2)) 
                pygame.display.update()
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
