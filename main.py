import pygame
from pygame.locals import QUIT

import cars_cache
import children_generator
import constants
from car import Car
from cars_cache import add_car, get_active_cars
from collisions import define_collision
from constants import NUMBER_OF_CARS
from game_setup import GameSetup
from options_menu import OptionsMenu, Button
from track import Track

game_setup = GameSetup()
options_menu = OptionsMenu(game_setup)
track = Track(game_setup.space, game_setup.width, game_setup.height)
for car_id in range(0, NUMBER_OF_CARS):
    car = Car(game_setup.space, game_setup.width, game_setup.height, car_id)
    add_car(car)
define_collision(game_setup.space)

kill_generation_button = Button(150, 10, 150, 20, text='Kill generation')

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if kill_generation_button.is_over(pos):
                for car in cars_cache.get_active_cars():
                    car.is_active = False

    children_generator.generate_children_if_needed()

    game_setup.space.step(1 / constants.FPS)
    game_setup.screen.fill((255, 255, 255))

    kill_generation_button.draw(game_setup.screen, pygame.font.Font(None, 18))
    text = pygame.font.Font(None, 20).render(f'Generation number: {children_generator.cars_generation}', True, (73, 73, 73))
    text_rect = text.get_rect(center=(300, 10))
    game_setup.screen.blit(text, text_rect)

    for car in get_active_cars():
        if car.crossed_checkpoints == Track.checkpoints_number:
            print(f'CHAMPION weights: {car.weights}')
        if not options_menu.is_active:
            car.set_car_angle()
            car.draw(game_setup.screen, constants.CAR_SPEED)
        else:
            car.draw(game_setup.screen, 0)

    track.draw(game_setup.screen)

    if options_menu.is_active:
        options_menu.draw()

    pygame.display.flip()

    game_setup.clock.tick(constants.FPS)
