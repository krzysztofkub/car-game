import pygame
import sys
from math import sqrt
from neural_network_calculation import NeuralNetwork  # Ensure correct import

# Initialize Pygame
pygame.init()

# Screen settings
screen_width, screen_height = 1200, 900
screen = pygame.display.set_mode((screen_width, screen_height))
background_color = (255, 255, 255)
neuron_color = (0, 0, 255)
line_color = (0, 0, 0)
text_color = (0, 0, 0)
font = pygame.font.SysFont('Arial', 15)


def is_mouse_over_neuron(mouse_pos, neuron_pos, radius=20):
    """Check if the mouse is over a neuron."""
    return sqrt((mouse_pos[0] - neuron_pos[0]) ** 2 + (mouse_pos[1] - neuron_pos[1]) ** 2) <= radius


def draw_neural_network(nn, mouse_pos):
    screen.fill(background_color)
    layer_positions = []  # To store the center positions of neurons for drawing connections
    spacing_x = screen_width // (len(nn.network_layers) + 1)

    # Iterate over layers to draw neurons
    for layer_index, layer in enumerate(nn.network_layers):
        neurons_in_layer = len(layer.neurons)
        spacing_y = screen_height // (neurons_in_layer + 1)
        neuron_positions = []

        for neuron_index, neuron in enumerate(layer.neurons):
            neuron_x = spacing_x * (layer_index + 1)
            neuron_y = spacing_y * (neuron_index + 1)
            neuron_positions.append((neuron_x, neuron_y))
            pygame.draw.circle(screen, neuron_color, (neuron_x, neuron_y), 20)

        layer_positions.append(neuron_positions)

    # Draw connections and show weights on hover
    for layer_index, (layer, positions) in enumerate(zip(nn.network_layers, layer_positions[:-1])):
        next_positions = layer_positions[layer_index + 1]
        for neuron_index, (neuron, pos) in enumerate(zip(layer.neurons, positions)):
            for next_neuron_index, next_pos in enumerate(next_positions):
                pygame.draw.line(screen, line_color, pos, next_pos, 1)
                if is_mouse_over_neuron(mouse_pos, pos, 20):
                    # Calculate midpoint of the line for displaying weight
                    midpoint = ((pos[0] + next_pos[0]) // 2, (pos[1] + next_pos[1]) // 2)
                    # Display weight text at the midpoint
                    weight_text = font.render(f"{neuron.weights[next_neuron_index]:.2f}", True, text_color)
                    screen.blit(weight_text, midpoint)

    pygame.display.flip()


# Create NeuralNetwork instance (example initialization)
nn = NeuralNetwork([0.5, -0.3, 0.7], [4, 4, 4, 4], [0.1, -0.2, 0.4, 0.6, -0.5, 0.9, 0.8, 0.7, -0.9, 0.3, -0.4, 0.2])
print(nn.calculate())

# Pygame loop
running = True
mouse_pos = (0, 0)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos

    draw_neural_network(nn, mouse_pos)

pygame.quit()
sys.exit()
