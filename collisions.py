import pygame

from car import Car


def define_collision(space):
    # Create car collision handler
    car_and_static_handler = space.add_collision_handler(0, 1)
    car_and_static_handler.begin = car_and_wall_collision

    # Create sensor collision handler
    sensor_handler = space.add_collision_handler(0, 2)
    sensor_handler.pre_solve = sensor_collision


def car_and_wall_collision(arbiter, space, data):
    print("Car collided with static line!")
    pygame.quit()
    exit()


def sensor_collision(arbiter, space, data):
    print("Sensor detected collision")
    return False
