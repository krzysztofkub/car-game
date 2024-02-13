import math
import random

import pygame
import pymunk
import pymunk.pygame_util

import constants
from driving_algorithm import drive


class Car:
    def __init__(self, space, width, height, id, position=(130, 700), angle=4.71):
        self.id = id
        self.is_active = True
        self.collision_type = constants.CAR_COLLISION_TYPE
        self.space = space
        self.car_body = self.create_car_body(position, angle, width, height)
        self.car_shape = self.create_car_shape(self.car_body, width, height)
        self.car_image = pygame.image.load("car.png")
        self.front_sensor_start = pymunk.Vec2d(0, 0)
        space.add(self.car_body, self.car_shape)
        self.sensor_shapes = []
        self.sensors = {}
        self.checkpoints_crossed_number = 0
        self.add_sensors()

    def create_car_body(self, position, angle, width, height):
        mass = 1
        moment = pymunk.moment_for_box(mass, (width / 40, height / 30))
        car_body = pymunk.Body(mass, moment)
        car_body.position = position
        car_body.angle = angle
        car_body.collision_type = self.collision_type
        return car_body

    @staticmethod
    def create_car_shape(car_body, width, height):
        car_shape = pymunk.Poly.create_box(car_body, (width / 40, height / 30))
        car_shape.friction = 0
        car_shape.collision_type = constants.CAR_COLLISION_TYPE
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

    def draw(self, screen):
        self.car_body.velocity = self.car_body.rotation_vector * constants.CAR_SPEED
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

    def set_car_angle(self):
        sensors = self.sensors
        temp_angle = self.car_body.angle
        self.car_body.angle = temp_angle + drive(sensors)

    def remove_from_space(self):
        for sensor in self.sensor_shapes:
            self.space.remove(sensor)
        for shape in self.car_body.shapes:
            self.space.remove(shape)

    def __repr__(self):
        return f'Car(id={self.id})'
