import pygame

from car import Car


def define_collision(space):
    # Create car collision handler
    car_and_static_handler = space.add_collision_handler(1, 0)
    car_and_static_handler.begin = car_and_wall_collision

    # Create sensor collision handler
    sensor_handler = space.add_collision_handler(0, 2)
    sensor_handler.begin = sensor_collision_begin


def car_and_wall_collision(arbiter, space, data):
    print("Car collided with static line!")
    pygame.quit()
    exit()


def sensor_collision_begin(arbiter, space, data):
    print("Sensor detected potential collision")
    return True  # Returning True continues processing this collision, False would ignore it
