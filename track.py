import pygame
import pymunk


class Track:
    def __init__(self, space, width, height):
        self.collision_type = 0
        self.static_lines = self.create_track(space, width, height, self.collision_type)
        self.height = height
        self.width = width

    @staticmethod
    def create_track(space, width, height, collision_type):
        static_lines = [
            pymunk.Segment(space.static_body, (50, 50), (50, height - 50), 5),
            pymunk.Segment(space.static_body, (50, height - 50), (width - 50, height - 50), 5),
            pymunk.Segment(space.static_body, (width - 50, height - 50), (width - 50, 50), 5),
            pymunk.Segment(space.static_body, (50, 50), (width - 50, 50), 5)
        ]

        for i, line in enumerate(static_lines):
            line.friction = 0
            line.color = (255, 0, 0)
            line.collision_type = collision_type
            space.add(line)

        return static_lines

    def to_pygame(self, p):
        return int(p.x), int(-p.y) + self.height

    def draw(self, screen):
        for line in self.static_lines:
            body = line.body
            pv1 = body.position + line.a.rotated(body.angle)
            pv2 = body.position + line.b.rotated(body.angle)
            p1 = self.to_pygame(pv1)
            p2 = self.to_pygame(pv2)
            pygame.draw.lines(screen, line.color, False, [p1, p2])