import pygame


def define_collision(space):
    car_and_static_handler = space.add_collision_handler(0, 1)
    car_and_static_handler.begin = car_and_wall_collision

    sensor_handler = space.add_collision_handler(0, 2)
    sensor_handler.pre_solve = sensor_collision_pre_solve


def car_and_wall_collision(arbiter, space, data):
    print("Car collided with static line!")
    pygame.quit()
    exit()


def sensor_collision_pre_solve(arbiter, space, data):
    sensor_shape = None
    for shape in arbiter.shapes:
        if hasattr(shape, "sensor_name"):  # Check if the shape is a sensor
            sensor_shape = shape
            break

    if sensor_shape is not None:
        contact_point = arbiter.contact_point_set.points[0].point_a
        sensor_start_pos = sensor_shape.body.position + sensor_shape.a.rotated(sensor_shape.body.angle)
        distance = sensor_start_pos.get_distance(contact_point)
        print(f"{sensor_shape.sensor_name} collided with track at distance: {distance}")
    return True
