import math
import random
import time

import cars_cache
import constants
from track import Track

cars_generation = 0


def get_two_champions():
    cars = cars_cache.get_cars()
    sorted_objects = sorted(cars, key=lambda car: len(car.crossed_checkpoints), reverse=True)
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
            car.last_time_crossed_checkpoint = time.time()
            car.is_active = True
        cars_generation += 1
        print(f'New generation: {cars_generation}')


def add_mutagen(weigths, a, b):
    number_of_mutated_weights = min(
        1 - max(len(a.crossed_checkpoints), len(b.crossed_checkpoints)) / Track.checkpoints_number,
        0.05) * len(weigths)
    weights_indexes = [random.randint(0, len(weigths) - 1) for _ in range(int(number_of_mutated_weights))]
    for index in weights_indexes:
        weigths[index] = random.uniform(-1, 1)
    return weigths


def crossover_weights(a, b):
    assert len(a.weights) == len(b.weights), "Arrays must have the same length"
    total_checkpoints = len(a.crossed_checkpoints) + len(b.crossed_checkpoints)
    a_percentage = len(a.crossed_checkpoints) / total_checkpoints
    crossed_over_weights = []
    for i in range(len(a.weights)):

        if random.random() < a_percentage:
            crossed_over_weights.append(a.weights[i])
        else:
            crossed_over_weights.append(b.weights[i])

    return add_mutagen(crossed_over_weights, a, b)
