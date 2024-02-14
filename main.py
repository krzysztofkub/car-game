import pygame
from pygame.locals import QUIT

import children_generator
from car import Car
from cars_cache import add_car, get_active_cars
from collisions import define_collision
from constants import NUMBER_OF_CARS
from game_setup import GameSetup
from track import Track

game_setup = GameSetup()
track = Track(game_setup.space, game_setup.width, game_setup.height)
for car_id in range(0, NUMBER_OF_CARS):
    car = Car(game_setup.space, game_setup.width, game_setup.height, car_id)
    add_car(car)
define_collision(game_setup.space)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    children_generator.generate_children_if_needed()

    # Update physics
    game_setup.space.step(1 / 60.0)
    # Clear the screen
    game_setup.screen.fill((255, 255, 255))

    for car in get_active_cars():
        car.set_car_angle()
        car.draw(game_setup.screen)

    track.draw(game_setup.screen)

    pygame.display.flip()

    game_setup.clock.tick(60)
