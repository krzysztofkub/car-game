import pygame
from pygame.locals import QUIT
from car import Car
from collisions import define_collision
from game_setup import setup_game
from track import Track

screen, space, clock, width, height = setup_game()
car = Car(space, width, height)
track = Track(space, width, height)
define_collision(space)

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
