import sys
 
import pygame
from pygame.locals import *


class Main:
    def __init__(self):
        pygame.init()
        self.fps = 60.0
        self.fpsClock = pygame.time.Clock()
        self.width = 1024
        self.height = 868
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.dt = 1/self.fps
        

    
    def run():
        # event handler
        # post processing
        # drawing picture
        pass

if __name__=="__main__":
    main = Main()
    main.run()