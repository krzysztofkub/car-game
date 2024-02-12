import random

import cars_cache


# TODO implement algorithm to pick two champions from track
def get_two_champions():
    return random.sample(range(len(cars_cache.get_cars())), 2)