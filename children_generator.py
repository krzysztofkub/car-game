from car import Car
import cars_cache
import constants


def get_two_champions():
    cars = cars_cache.get_cars()
    sorted_objects = sorted(cars, key=lambda car: len(car.crossed_checkpoints), reverse=True)
    return sorted_objects[:2]


def create_next_generation_cars(parents):
    return [Car.from_parents(parents[0], parents[1], i) for i in range(0, constants.NUMBER_OF_CARS)]


def generate_children_if_needed():
    active_cars = cars_cache.get_active_cars()
    if not active_cars:
        parents = get_two_champions()
        next_generation_cars = create_next_generation_cars(parents)
        cars_cache.update_cars(next_generation_cars)
