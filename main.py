import pygame
from pygame.locals import QUIT
from car import Car
from collisions import define_collision
from game_setup import GameSetup
from track import Track

game_setup = GameSetup()
car = Car(game_setup.space, game_setup.width, game_setup.height)
track = Track(game_setup.space, game_setup.width, game_setup.height)
define_collision(game_setup.space)

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
    game_setup.space.step(1 / 60.0)

    # Clear the screen
    game_setup.screen.fill((255, 255, 255))

    car.update(game_setup.screen)
    track.draw(game_setup.screen)

    pygame.display.flip()

    game_setup.clock.tick(60)
