cars = []
cars_generation = 0


def remove_car(car_body):
    filtered_cars = [car for car in cars if car.car_body == car_body]
    if filtered_cars:
        car_to_be_removed = filtered_cars[0]
        car_to_be_removed.remove_from_space()
        car_to_be_removed.is_active = False


def get_active_cars():
    return [car for car in cars if car.is_active]


def add_car(car):
    cars.append(car)


def get_car(car_id):
    filtered_cars = [car for car in cars if car.id == car_id]
    if filtered_cars:
        return filtered_cars[0]


def get_cars():
    return cars


def update_cars(new_cars):
    global cars, cars_generation
    cars_generation += 1
    cars = new_cars
    print(f'New generation: {cars_generation}')
