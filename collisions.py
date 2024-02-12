import pygame

import constants
from cars_cache import remove_car, get_car


def define_collision(space):
    cars_collision_handler = space.add_collision_handler(constants.CAR_COLLISION_TYPE, constants.CAR_COLLISION_TYPE)
    cars_collision_handler.begin = lambda arbiter, space, data: False

    car_and_wall_collision_handler = space.add_collision_handler(constants.TRACK_COLLISION_TYPE, constants.CAR_COLLISION_TYPE)
    car_and_wall_collision_handler.begin = car_and_wall_collision

    sensor_handler = space.add_collision_handler(constants.TRACK_COLLISION_TYPE, constants.SENSOR_COLLISION_TYPE)
    sensor_handler.begin = sensor_begin
    sensor_handler.pre_solve = calculate_sensor_length
    sensor_handler.separate = sensor_separate


def car_and_wall_collision(arbiter, space, data):
    print("Car collided with static line!")
    car_body = None
    for shape in arbiter.shapes:
        if shape.collision_type == 1:
            car_body = shape.body
    if car_body is not None:
        remove_car(car_body)

    return True


def sensor_begin(arbiter, space, data):
    sensor_shape = None
    for shape in arbiter.shapes:
        if hasattr(shape, "sensor_name"):  # Check if the shape is a sensor
            sensor_shape = shape
            break
    if sensor_shape is not None:
        print(f"{sensor_shape.sensor_name} BEGIN")
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
        print(f"{sensor_shape.sensor_name} FINISH")
        car = get_car_by_sensor_shape(sensor_shape)
        if car is not None and sensor_shape.sensor_name in car.sensors:
            car.sensors.pop(sensor_shape.sensor_name)

    return True


def get_car_by_sensor_shape(sensor_shape):
    car_id = int(sensor_shape.sensor_name.split(":")[1])
    return get_car(car_id)
