import math

import pygame
from pygame.locals import QUIT
import pymunk.pygame_util


# Collision handler callback function
def car_and_static_collision(arbiter, space, data):
    # You can add code here to perform actions when the car collides with a static line
    print("Car collided with static line!")
    pygame.quit()
    exit()


def to_pygame(p):
    return int(p.x), int(-p.y) + height


# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 2000, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PyMunk Car Game")

# Load car image
car_image = pygame.image.load("car.png")

# Create a PyMunk space
space = pymunk.Space()
space.gravity = (0, 0)

# Create car body
car_body = pymunk.Body(1, pymunk.moment_for_box(1, (50, 30)))
car_body.collision_type = 0
car_shape = pymunk.Poly.create_box(car_body, (50, 30))
car_shape.friction = 0

# Set position
car_body.position = (400, 300)
car_body.angle = 0  # Set the initial angle to 0

# Add car to the space
# space.add(car_body, car_shape)

track_width = 20
static_lines = [
    pymunk.Segment(space.static_body, (200, 200), (400, 200), track_width),  # Straight segment
    pymunk.Segment(space.static_body, (400, 200), (500, 300), track_width),  # Right turn
    pymunk.Segment(space.static_body, (500, 300), (400, 400), track_width),  # Left turn
    pymunk.Segment(space.static_body, (400, 400), (300, 300), track_width),  # Right turn
    pymunk.Segment(space.static_body, (300, 300), (200, 400), track_width),  # Left turn
    pymunk.Segment(space.static_body, (200, 400), (300, 500), track_width),  # Right turn
    pymunk.Segment(space.static_body, (300, 500), (500, 500), track_width),  # Left turn
    pymunk.Segment(space.static_body, (500, 500), (600, 400), track_width),  # Right turn
    pymunk.Segment(space.static_body, (600, 400), (500, 300), track_width),  # Left turn
    pymunk.Segment(space.static_body, (500, 300), (400, 200), track_width),  # Right turn
    pymunk.Segment(space.static_body, (200, 200), (400, 200), track_width),  # Connect back to the start
]

for i, line in enumerate(static_lines):
    line.friction = 0
    line.color = (255, 0, 0)
    line.collision_type = 1
    space.add(line)

# Pygame clock
clock = pygame.time.Clock()

# Create a collision handler
car_and_static_handler = space.add_collision_handler(0, 1)
car_and_static_handler.begin = car_and_static_collision

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    # Rotate the car when the LEFT arrow is pressed
    if keys[pygame.K_RIGHT]:
        car_body.angle += 0.1

    # Rotate the car when the RIGHT arrow is pressed
    if keys[pygame.K_LEFT]:
        car_body.angle -= 0.1

    # Set the car's velocity based on its direction
    speed = 100
    car_body.velocity = car_body.rotation_vector * speed

    # Update physics
    space.step(1 / 60.0)

    # Explicitly set angular velocity to zero to prevent automatic addition
    car_body.angular_velocity = 0

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw car image
    rotated_car_image = pygame.transform.rotate(car_image, -car_body.angle * 180 / math.pi)
    scale_factor = 0.5
    scaled_car_image = pygame.transform.scale(rotated_car_image, (
        int(rotated_car_image.get_width() * scale_factor),
        int(rotated_car_image.get_height() * scale_factor)
    ))
    screen.blit(scaled_car_image, car_body.position - scaled_car_image.get_rect().center)

    # Draw static lines
    for line in static_lines:
        body = line.body
        pv1 = body.position + line.a.rotated(body.angle)
        pv2 = body.position + line.b.rotated(body.angle)
        p1 = to_pygame(pv1)
        p2 = to_pygame(pv2)
        pygame.draw.lines(screen, line.color, False, [p1, p2])

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
