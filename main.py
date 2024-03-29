import pygame
from pygame.locals import QUIT

import children_generator
import constants
from car import Car
from cars_cache import add_car, get_active_cars
from collisions import define_collision
from constants import NUMBER_OF_CARS
from game_setup import GameSetup
from options_menu import OptionsMenu
from track import Track

game_setup = GameSetup()
options_menu = OptionsMenu(game_setup)
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
        if options_menu.is_active:
            options_menu.handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                options_menu.toggle()

    children_generator.generate_children_if_needed()

    game_setup.space.step(1 / 60.0)
    game_setup.screen.fill((255, 255, 255))

    for car in get_active_cars():
        if not options_menu.is_active:
            car.set_car_angle()
            car.draw(game_setup.screen, constants.CAR_SPEED)
        else:
            car.draw(game_setup.screen, 0)

    track.draw(game_setup.screen)

    if options_menu.is_active:
        options_menu.draw()

    pygame.display.flip()

    game_setup.clock.tick(60)
