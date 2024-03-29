import random

import pygame

import constants


# TODO implement driving alogrithm
def drive(sensors):
    if constants.MANUAL_DRIVE:
        return manual_drive()
    else:
        return auto_drive(sensors)


def auto_drive(sensors):
    number_of_sensors = len(sensors)
    if number_of_sensors == 0:
        return random.uniform(-0.05, 0.05)
    if number_of_sensors == 1:
        return random.uniform(-0.1, 0.1)
    if number_of_sensors == 2:
        return random.uniform(-0.2, 0.2)
    if number_of_sensors == 3:
        return random.uniform(-0.3, 0.3)
    if number_of_sensors == 4:
        return random.uniform(-0.4, 0.4)
    if number_of_sensors == 5:
        return random.uniform(-0.8, 0.8)
    return 0


def manual_drive():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        return 0.1
    if keys[pygame.K_LEFT]:
        return -0.1
    return 0
