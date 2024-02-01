import math

import pygame
import pymunk


class Car:
    def __init__(self, space, width, height, position=(100, 100), angle=0, collision_type=1):
        self.space = space
        self.car_body = self.create_car_body(position, angle, width, height, collision_type)
        self.car_shape = self.create_car_shape(self.car_body, width, height)
        self.space.add(self.car_body, self.car_shape)
        self.car_image = pygame.image.load("car.png")
        self.collision_type = collision_type

    @staticmethod
    def create_car_body(position, angle, width, height, collision_type):
        mass = 1
        moment = pymunk.moment_for_box(mass, (width/40, height/30))
        car_body = pymunk.Body(mass, moment)
        car_body.position = position
        car_body.angle = angle
        car_body.collision_type = collision_type
        return car_body

    @staticmethod
    def create_car_shape(car_body, width, height):
        car_shape = pymunk.Poly.create_box(car_body, (width/40, height/30))
        car_shape.friction = 0
        return car_shape

    def update(self, screen):
        speed = 100
        self.car_body.velocity = self.car_body.rotation_vector * speed
        self.car_body.angular_velocity = 0

        # Draw car image
        rotated_car_image = pygame.transform.rotate(self.car_image, -self.car_body.angle * 180 / math.pi)
        scale_factor = 0.5
        scaled_car_image = pygame.transform.scale(rotated_car_image, (
            int(rotated_car_image.get_width() * scale_factor),
            int(rotated_car_image.get_height() * scale_factor)
        ))
        screen.blit(scaled_car_image, self.car_body.position - scaled_car_image.get_rect().center)
