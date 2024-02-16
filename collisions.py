import time

import pygame
import pymunk
import constants
from cars_cache import deactivate_car, get_car


def define_collision(space):
    cars_collision_handler = space.add_collision_handler(constants.CAR_COLLISION_TYPE, constants.CAR_COLLISION_TYPE)
    cars_collision_handler.begin = lambda arbiter, space, data: False

    car_and_wall_collision_handler = space.add_collision_handler(constants.TRACK_COLLISION_TYPE,
                                                                 constants.CAR_COLLISION_TYPE)
    car_and_wall_collision_handler.begin = car_and_wall_collision

    car_and_checkpoint_collision_handler = space.add_collision_handler(constants.CHECKPOINT_COLLISION_TYPE,
                                                                       constants.CAR_COLLISION_TYPE)
    car_and_checkpoint_collision_handler.begin = car_and_checkpoint_collision

    sensor_handler = space.add_collision_handler(constants.TRACK_COLLISION_TYPE, constants.SENSOR_COLLISION_TYPE)
    sensor_handler.begin = sensor_begin
    sensor_handler.pre_solve = calculate_sensor_length
    sensor_handler.separate = sensor_separate


def car_and_checkpoint_collision(arbiter, space, data):
    car_shape = None
    checkpoint_shape = None
    for shape in arbiter.shapes:
        if hasattr(shape, "car_id"):
            car_shape = shape
        if hasattr(shape, "checkpoint_id"):
            checkpoint_shape = shape

    if car_shape is not None and checkpoint_shape is not None:
        car_id = int(car_shape.car_id)
        car = get_car(car_id)
        if checkpoint_shape.checkpoint_id not in car.crossed_checkpoints:
            car.crossed_checkpoints.add(checkpoint_shape.checkpoint_id)
            car.last_time_crossed_checkpoint = time.time()

    return False


def car_and_wall_collision(arbiter, space, data):
    car_body = None
    for shape in arbiter.shapes:
        if shape.collision_type == 1:
            car_body = shape.body
    if car_body is not None:
        deactivate_car(car_body)

    return True


def sensor_begin(arbiter, space, data):
    sensor_shape = None
    for shape in arbiter.shapes:
        if hasattr(shape, "sensor_name"):  # Check if the shape is a sensor
            sensor_shape = shape
            break
    if sensor_shape is not None:
        car = get_car_by_sensor_shape(sensor_shape)
        if car is not None:
            car.sensors[sensor_shape.sensor_name] = constants.SENSOR_LENGTH
    return True


def calculate_sensor_length(arbiter, space, data):
    sensor_shape = None
    for shape in arbiter.shapes:
        if hasattr(shape, "sensor_name"):  # Check if the shape is a sensor
            sensor_shape = shape
            break

    if sensor_shape is not None:
        contact_point = arbiter.contact_point_set.points[0].point_a
        sensor_start_pos = sensor_shape.body.position + sensor_shape.a.rotated(sensor_shape.body.angle)
        distance = sensor_start_pos.get_distance(contact_point)
        car = get_car_by_sensor_shape(sensor_shape)
        if car is not None:
            car.sensors[sensor_shape.sensor_name] = distance
    return True


def sensor_separate(arbiter, space, data):
    sensor_shape = None
    for shape in arbiter.shapes:
        if hasattr(shape, "sensor_name"):  # Check if the shape is a sensor
            sensor_shape = shape
            break

    if sensor_shape is not None:
        car = get_car_by_sensor_shape(sensor_shape)
        if car is not None and sensor_shape.sensor_name in car.sensors:
            car.sensors.pop(sensor_shape.sensor_name)

    return True


def get_car_by_sensor_shape(sensor_shape):
    car_id = int(sensor_shape.sensor_name.split(":")[1])
    return get_car(car_id)
