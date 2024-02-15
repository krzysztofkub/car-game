import pygame
import sys
import random
from functools import reduce
from math import sqrt

pygame.init()


screen_width = 1200
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))


background_color = (255, 255, 255)  # White
neuron_color = (0, 0, 255)  # Blue
line_color = (0, 0, 0)  # Black
text_color = (0, 0, 0)  # Black


networks_grid = [3, 2, 3]

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

pygame.font.init()
font = pygame.font.SysFont('Arial', 15)


def is_mouse_over_neuron(mouse_pos, neuron_pos, radius=20):
    distance = sqrt((mouse_pos[0] - neuron_pos[0]) ** 2 + (mouse_pos[1] - neuron_pos[1]) ** 2)
    return distance <= radius


def draw_neural_network(mouse_pos):
    screen.fill(background_color)
    neuron_positions = [[] for _ in range(len(networks_grid))]
    weight_index = 0

    max_neurons = max(networks_grid)
    neuron_radius = 20
    total_vertical_space = (max_neurons - 1) * neuron_radius * 3
    start_y = (screen_height - total_vertical_space) // 2

    # Draw neurons
    for layer_index, layer_size in enumerate(networks_grid):
        x = (layer_index + 1) * (screen_width // (len(networks_grid) + 1))
        for neuron_index in range(layer_size):
            if layer_size == max_neurons:
                y = start_y + neuron_index * (neuron_radius * 3)
            else:
                offset = (max_neurons - layer_size) * neuron_radius * 1.5
                y = start_y + offset + neuron_index * (neuron_radius * 3)
            pygame.draw.circle(screen, neuron_color, (x, y), neuron_radius)
            neuron_positions[layer_index].append((x, y))

    # Draw lines and conditionally display weights in the middle
    for layer_index, layer_positions in enumerate(neuron_positions[:-1]):
        for start_neuron_index, start_pos in enumerate(layer_positions):
            for end_neuron_index, end_pos in enumerate(neuron_positions[layer_index + 1]):
                pygame.draw.line(screen, line_color, start_pos, end_pos, 1)
                midpoint = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                if is_mouse_over_neuron(mouse_pos, start_pos) or is_mouse_over_neuron(mouse_pos, end_pos):
                    weight_text = font.render(f"{weights[weight_index]:.2f}", True, text_color)
                    screen.blit(weight_text, midpoint)  # Display at the midpoint of the line for selected connection
                weight_index += 1

    pygame.display.flip()


running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_neural_network(mouse_pos)

pygame.quit()
sys.exit()
