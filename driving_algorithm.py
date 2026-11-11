import random
import time

import pygame

import constants
from neural_network_calculation import NeuralNetwork


def get_sensors_lengths_for_calculation(car):
    sensors_values = [sensor / 1000 for sensor in list(car.sensors.values())]
    while len(sensors_values) < constants.SENSORS_NUMBER:
        sensors_values.append(constants.SENSOR_LENGTH * 3 / 1000)
    return sensors_values


def set_car_angle(car):
    sensors = get_sensors_lengths_for_calculation(car)
    temp_angle = car.car_body.angle
    car.car_body.angle = temp_angle + drive(sensors, car)


def drive(sensors, car):
    if constants.MANUAL_DRIVE:
        return manual_drive()
    else:
        return auto_drive(sensors, car)


def auto_drive(sensors, car):
    nn = NeuralNetwork(sensors, constants.NETWORK_HIDDEN_LAYERS, car.weights)
    return nn.calculate()[0]


def manual_drive():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        return 0.1
    if keys[pygame.K_LEFT]:
        return -0.1
    return 0
