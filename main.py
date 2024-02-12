import pygame
from pygame.locals import QUIT

from car import Car
from cars_cache import add_car, get_active_cars
from champions_picking_alogrithm import get_two_champions
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

    # Check for finished simulation
    active_cars = get_active_cars()
    if not active_cars:
        parents = get_two_champions()
        print(f'Najlepsze samochody to: {parents}')
        break

    # Update physics
    game_setup.space.step(1 / 60.0)
    # Clear the screen
    game_setup.screen.fill((255, 255, 255))

    for car in active_cars:
        car.set_car_angle()
        car.draw(game_setup.screen)

    track.draw(game_setup.screen)

    pygame.display.flip()

    game_setup.clock.tick(60)
