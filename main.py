import random

import pygame
from pygame.locals import QUIT

import collisions
from car import Car
from collisions import define_collision
from game_setup import GameSetup
from track import Track

game_setup = GameSetup()
car = Car(game_setup.space, game_setup.width, game_setup.height)
track = Track(game_setup.space, game_setup.width, game_setup.height)
define_collision(game_setup.space)


def set_car_angle() -> float:
    sensors = collisions.get_active_sensors()
    if sensors != {}:
        temp_angle = car.car_body.angle
        car.car_body.angle = temp_angle + calculate_move()


def calculate_move():
    return random.uniform(-0.3, 0.3)


# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    set_car_angle()

    # Update physics
    game_setup.space.step(1 / 60.0)

    # Clear the screen
    game_setup.screen.fill((255, 255, 255))

    car.update(game_setup.screen)
    track.draw(game_setup.screen)

    pygame.display.flip()

    game_setup.clock.tick(60)
