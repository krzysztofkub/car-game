import pygame
import pymunk

import constants


class GameSetup:
    def __init__(self):
        pygame.init()
        self.width, self.height = constants.SCREEN_SIZE
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("PyMunk Car Game")
        self.space = self.create_space()
        self.clock = pygame.time.Clock()

    def create_space(self):
        space = pymunk.Space()
        space.gravity = (0, 0)
        return space
