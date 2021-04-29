# function that ties the Model-View_controller classes together
import pygame, sys
from pygame.locals import *
import random, time

from the_ark_view import ArkView
from the_ark_game import ArkGame
from the_ark_controller import ArkController

def main():
    pygame.init()
    
    FPS = 60
    FramePerSec = pygame.time.Clock()

    BLUE  = (0, 0, 255)
    RED   = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    #this block of code can be a View class method that starts the screen
    DISPLAYSURF = pygame.display.set_mode((400,600))
    DISPLAYSURF.fill(WHITE)
    pygame.display.set_caption("Game")
    
    # these will eventually be class attributes of the Game class
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 600
    SPEED = 5
    
    
    game = ArkGame()
    game_view = ArkView(game)
    player = ArkController(game)
    
    
 
    while True:     
        for event in pygame.event.get():              
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        player.move()
        
        # this block of code could be an "update_view" method that paint the screen           white and redraw the player; this is definitely a View method
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(player.image, player.rect)
        pygame.display.update()
        
        FramePerSec.tick(FPS)

if __name__ == "__main__":
    main()
