import pygame
import pymunk


class GameSetup:
    def __init__(self):
        pygame.init()
        self.width, self.height = self.get_screen_size()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("PyMunk Car Game")
        self.space = self.create_space()
        self.clock = pygame.time.Clock()

    def create_space(self):
        space = pymunk.Space()
        space.gravity = (0, 0)
        return space

    @staticmethod
    def get_screen_size():
        return 2000, 900
