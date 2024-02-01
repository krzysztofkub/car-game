import math

import pygame
from pygame.locals import QUIT
import pymunk.pygame_util

from car import Car
from track import Track


# Collision handler callback function
def car_and_wall_collision(arbiter, space, data):
    print("Car collided with static line!")
    pygame.quit()
    exit()


# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 2000, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PyMunk Car Game")

# Create a PyMunk space
space = pymunk.Space()
space.gravity = (0, 0)

# Pygame clock
clock = pygame.time.Clock()

# Create a collision handler
car_and_static_handler = space.add_collision_handler(0, 1)
car_and_static_handler.begin = car_and_wall_collision

car = Car(space, width, height)
track = Track(space, width, height)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        car.car_body.angle += 0.1
    if keys[pygame.K_LEFT]:
        car.car_body.angle -= 0.1

    # Update physics
    space.step(1 / 60.0)

    # Clear the screen
    screen.fill((255, 255, 255))

    car.update(screen)
    track.draw(screen)

    pygame.display.flip()

    clock.tick(60)
