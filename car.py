import math
import random
import time

import pygame
import pymunk
import pymunk.pygame_util

import constants
from driving_algorithm import drive


class Car:

    def __init__(self, space, width, height, id, weights, position=constants.STARTING_POSITION, angle=constants.STARTING_ANGLE):
        self.id = id
        self.is_active = True
        self.collision_type = constants.CAR_COLLISION_TYPE
        self.space = space
        self.screen_width = width
        self.screen_height = height
        self.car_body = self.create_car_body(position, angle)
        self.car_shape = self.create_car_shape(self.car_body)
        self.car_image = pygame.image.load("car.png")
        self.front_sensor_start = pymunk.Vec2d(0, 0)
        space.add(self.car_body, self.car_shape)
        self.sensor_shapes = []
        self.sensors = {}
        self.crossed_checkpoints = set()
        self.last_time_crossed_checkpoint = None
        self.spawn_time = time.time()
        self.finish_time = None
        self.add_sensors()
        self.weights = weights

    def create_car_body(self, position, angle):
        mass = 1
        moment = pymunk.moment_for_box(mass, (self.screen_width / 70, self.screen_height / 50))
        car_body = pymunk.Body(mass, moment)
        car_body.position = position
        car_body.angle = angle
        car_body.collision_type = self.collision_type
        car_body.car_id = self.id
        return car_body

    def create_car_shape(self, car_body):
        car_shape = pymunk.Poly.create_box(car_body, (self.screen_width / 70, self.screen_height / 50))
        car_shape.friction = 0
        car_shape.collision_type = constants.CAR_COLLISION_TYPE
        car_shape.car_id = self.id
        return car_shape

    def add_sensors(self):
        offset_distance = 0
        sensors_number = constants.SENSORS_NUMBER
        angle_step = 180 / (sensors_number - 1) if sensors_number > 1 else 0

        for i in range(sensors_number):
            angle = math.radians(-90 + i * angle_step)
            end_x = math.cos(angle) * constants.SENSOR_LENGTH
            end_y = math.sin(angle) * constants.SENSOR_LENGTH

            sensor_name = f"Sensor {i + 1}:{self.id}"
            sensor_shape = pymunk.Segment(
                self.car_body,
                (offset_distance, 0),
                (offset_distance + end_x, end_y),
                constants.SENSOR_WIDTH)
            sensor_shape.sensor = True
            sensor_shape.collision_type = constants.SENSOR_COLLISION_TYPE
            sensor_shape.sensor_name = sensor_name
            self.space.add(sensor_shape)
            self.sensor_shapes.append(sensor_shape)

    def draw(self, screen, car_speed):
        self.car_body.velocity = self.car_body.rotation_vector * car_speed
        self.car_body.angular_velocity = 0

        # Draw car image
        rotated_car_image = pygame.transform.rotate(self.car_image, -self.car_body.angle * 180 / math.pi)
        scale_factor = 0.5
        scaled_car_image = pygame.transform.scale(rotated_car_image, (
            int(rotated_car_image.get_width() * scale_factor),
            int(rotated_car_image.get_height() * scale_factor)
        ))
        screen.blit(scaled_car_image, self.car_body.position - scaled_car_image.get_rect().center)

        # Draw all sensor lines
        if constants.DRAW_SENSORS:
            for sensor_shape in self.sensor_shapes:
                # Calculate the sensor's absolute start and end points
                sensor_start_pos = self.car_body.position + sensor_shape.a.rotated(self.car_body.angle)
                sensor_end_pos = self.car_body.position + sensor_shape.b.rotated(self.car_body.angle)

                # Convert Pymunk positions to Pygame positions
                sensor_start_pygame = pymunk.pygame_util.to_pygame(sensor_start_pos, screen)
                sensor_end_pygame = pymunk.pygame_util.to_pygame(sensor_end_pos, screen)

                # Draw the sensor lines
                pygame.draw.line(screen, (255, 0, 0), sensor_start_pygame, sensor_end_pygame, constants.SENSOR_WIDTH)

    def deactivate_car(self):
        self.is_active = False
        self.finish_time = time.time()

    def __repr__(self):
        return f'Car(id={self.id})'
