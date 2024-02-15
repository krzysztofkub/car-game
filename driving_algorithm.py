import random

import pygame

import constants
from neural_network_calculation import NeuralNetwork


# TODO implement driving alogrithm
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
