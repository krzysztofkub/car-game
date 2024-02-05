import math

import pygame
import pymunk
import pymunk.pygame_util


class Car:
    def __init__(self, space, width, height, position=(100, 100), angle=0):
        self.collision_type = 1
        self.space = space
        self.car_body = self.create_car_body(position, angle, width, height, self.collision_type)
        self.car_shape = self.create_car_shape(self.car_body, width, height, self.collision_type)
        self.car_image = pygame.image.load("car.png")
        self.front_sensor_start = pymunk.Vec2d(0, 0)  # Convert to Vec2d
        self.sensor_length = 100  # Length of the sensor lines
        space.add(self.car_body, self.car_shape)
        self.sensor_shapes = []
        self.sensors_number = 3
        self.add_sensors()



    @staticmethod
    def create_car_body(position, angle, width, height, collision_type):
        mass = 1
        moment = pymunk.moment_for_box(mass, (width / 40, height / 30))
        car_body = pymunk.Body(mass, moment)
        car_body.position = position
        car_body.angle = angle
        car_body.collision_type = collision_type
        return car_body

    @staticmethod
    def create_car_shape(car_body, width, height, collision_type):
        car_shape = pymunk.Poly.create_box(car_body, (width / 40, height / 30))
        car_shape.friction = 0
        car_shape.collision_type = collision_type
        return car_shape

    def add_sensors(self):
        sensor_length = 100
        sensor_width = 5
        offset_distance = 0
        angle_step = 180 / (self.sensors_number - 1) if self.sensors_number > 1 else 0

        for i in range(self.sensors_number):
            angle = math.radians(-90 + i * angle_step)
            end_x = math.cos(angle) * sensor_length
            end_y = math.sin(angle) * sensor_length

            sensor_name = f"Sensor {i + 1}"
            sensor_shape = pymunk.Segment(
                self.car_body,
                (offset_distance, 0),
                (offset_distance + end_x, end_y),
                sensor_width)
            sensor_shape.sensor = True
            sensor_shape.collision_type = 2
            sensor_shape.sensor_name = sensor_name
            self.space.add(sensor_shape)
            self.sensor_shapes.append(sensor_shape)

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

        # Draw all sensor lines
        for sensor_shape in self.sensor_shapes:
            # Calculate the sensor's absolute start and end points
            sensor_start_pos = self.car_body.position + sensor_shape.a.rotated(self.car_body.angle)
            sensor_end_pos = self.car_body.position + sensor_shape.b.rotated(self.car_body.angle)

            # Convert Pymunk positions to Pygame positions
            sensor_start_pygame = pymunk.pygame_util.to_pygame(sensor_start_pos, screen)
            sensor_end_pygame = pymunk.pygame_util.to_pygame(sensor_end_pos, screen)

            # Draw the sensor lines
            pygame.draw.line(screen, (255, 0, 0), sensor_start_pygame, sensor_end_pygame, 2)
