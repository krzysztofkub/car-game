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
        self.add_sensors()
        self.front_sensor_start = pymunk.Vec2d(0, 0)  # Convert to Vec2d
        self.sensor_length = 100  # Length of the sensor lines

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

    def add_sensors(self):
        sensor_length = 100  # Length of the sensor lines
        sensor_width = 5  # Thickness of the sensors (for visibility, can be 1 for a line)
        offset_distance = 0  # Distance from the center of the car to where the sensors start

        # Front sensor
        front_sensor_shape = pymunk.Segment(
            self.car_body,
            (-offset_distance, 0),
            (-offset_distance + sensor_length, 0),
            sensor_width)
        front_sensor_shape.sensor = True
        front_sensor_shape.collision_type = 2
        self.space.add(front_sensor_shape)

    @staticmethod
    def sensor_collision_begin(arbiter, space, data):
        print("Sensor detected potential collision")
        return True  # Returning True continues processing this collision, False would ignore it

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
        # Calculate the sensor's absolute start and end points
        sensor_start_pos = self.car_body.position + self.front_sensor_start.rotated(self.car_body.angle)
        sensor_end_pos = sensor_start_pos + pymunk.Vec2d(self.sensor_length, 0).rotated(self.car_body.angle)

        # Convert Pymunk positions to Pygame positions
        sensor_start_pygame = pymunk.pygame_util.to_pygame(sensor_start_pos, screen)
        sensor_end_pygame = pymunk.pygame_util.to_pygame(sensor_end_pos, screen)

        # Draw the sensor lines
        pygame.draw.line(screen, (255, 0, 0), sensor_start_pygame, sensor_end_pygame, 2)  # Red sensor lines
