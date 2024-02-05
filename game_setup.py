import pygame
import pymunk


def setup_game():
    pygame.init()
    # Set up the screen
    width, height = 2000, 900
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("PyMunk Car Game")
    # Create a PyMunk space
    space = pymunk.Space()
    space.gravity = (0, 0)
    clock = pygame.time.Clock()
    return screen, space, clock, width, height
