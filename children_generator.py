import math
import random
import time

import cars_cache
import constants

cars_generation = 0


def get_car_lifespan(car):
    return car.finish_time - car.spawn_time


def get_two_champions():
    cars = cars_cache.get_cars()

    sorted_objects = sorted(cars, key=lambda car: (len(car.crossed_checkpoints), -get_car_lifespan(car)), reverse=True)
    return sorted_objects[:2]


def generate_children_if_needed():
    global cars_generation
    active_cars = cars_cache.get_active_cars()
    if not active_cars:
        parents = get_two_champions()
        cars = cars_cache.get_cars()
        for car in cars:
            car.car_body.position = constants.STARTING_POSITION
            car.car_body.angle = constants.STARTING_ANGLE
            car.weights = crossover_weights(parents[0], parents[1])
            car.spawn_time = time.time()
            car.finish_time = None
            car.crossed_checkpoints = set()
            car.last_time_crossed_checkpoint = None
            car.is_active = True
        cars_generation += 1
        print(f'New generation: {cars_generation}')


def add_mutagen(weights):
    for i in range(len(weights)):
        if random.random() < constants.MUTATION_RATE:
            weights[i] = random_weight()
    return weights


def crossover_weights(a, b):
    assert len(a.weights) == len(b.weights), "Arrays must have the same length"
    midpoint = math.floor(random.randint(1, len(a.weights)))
    crossed_over_weights = a.weights[:midpoint + 1] + b.weights[midpoint + 1:]
    return add_mutagen(crossed_over_weights)


def generate_weights():
    total_weights_needed = 0
    input_size = constants.SENSORS_NUMBER
    for layer_size in constants.NETWORK_HIDDEN_LAYERS + [1]:
        total_weights_needed += layer_size * input_size
        input_size = layer_size
    return [random_weight() for _ in range(total_weights_needed)]


def random_weight():
    return random.uniform(constants.WEIGHTS_RANGE[0], constants.WEIGHTS_RANGE[1])