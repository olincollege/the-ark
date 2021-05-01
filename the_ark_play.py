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

    BLUE  = (0, 0, 255)
    RED   = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    game = ArkGame()
    game_view = ArkView(game)
    player = ArkController(game)
    
    #this block of code can be a View class method that starts the screen
    DISPLAYSURF = pygame.display.set_mode((game.SCREEN_WIDTH, game.SCREEN_HEIGHT))
    DISPLAYSURF.fill(WHITE)
    pygame.display.set_caption("Game")
    
    # these will eventually be class attributes of the Game class
    
    imageList1 = [Block(game, 92, 92 + (y_pos*61)) for y_pos in range(0,10,1)]
    imageList2 = [Block(game, 92 + (x_pos*61), 92) for x_pos in range(1,3,1)]
    imageList3 = [Block(game, 92 + (x_pos*61), 641) for x_pos in range(1,3,1)]
    blocks = pygame.sprite.Group(imageList1, imageList2, imageList3)
    imageList4 = [Block(game, 519, 92 + (y_pos*61)) for y_pos in range(0,10,1)]
    imageList5 = [Block(game, 336 + (x_pos*61), 92) for x_pos in range(1,3,1)]
    imageList6 = [Block(game, 336 + (x_pos*61), 641) for x_pos in range(1,3,1)]
    imageList = imageList1+imageList2+imageList3+imageList4+imageList5+imageList6
    blocks = pygame.sprite.Group(imageList)
    
    all_sprites = pygame.sprite.Group(blocks)
    all_sprites.add(player)
    
 
    while True:     
        for event in pygame.event.get():              
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        
        
        # this block of code could be an "update_view" method that paint the screen           white and redraw the player; this is definitely a View method
        DISPLAYSURF.fill(BLUE)
        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
        player.move(game)
        pygame.display.update()
        
        FramePerSec.tick(FPS)

if __name__ == "__main__":
    main()
