import pygame

import constants

sensors = {}


def define_collision(space):
    car_and_wall_collision_handler = space.add_collision_handler(0, 1)
    car_and_wall_collision_handler.begin = car_and_wall_collision

    sensor_handler = space.add_collision_handler(0, 2)
    sensor_handler.begin = store_sensor
    sensor_handler.pre_solve = calculate_sensor_length
    sensor_handler.separate = remove_sensor


def car_and_wall_collision(arbiter, space, data):
    print("Car collided with static line!")
    pygame.quit()
    exit()


def store_sensor(arbiter, space, data):
    sensor_shape = None
    for shape in arbiter.shapes:
        if hasattr(shape, "sensor_name"):  # Check if the shape is a sensor
            sensor_shape = shape
            break
    if sensor_shape is not None:
        sensors[sensor_shape.sensor_name] = constants.SENSOR_LENGTH


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
        sensors[sensor_shape.sensor_name] = distance
        print(f"{sensor_shape.sensor_name} collided with track at distance: {distance}")
    return True


def remove_sensor(arbiter, space, data):
    sensor_name = None
    for shape in arbiter.shapes:
        if hasattr(shape, "sensor_name"):  # Check if the shape is a sensor
            sensor_name = shape
            break

    if sensor_name is not None:
        del sensors[sensor_name.sensor_name]
    return True


def get_active_sensors():
    return sensors
