import pygame
import pymunk

from constants import TRACK_CHOICE


class Track:
    def __init__(self, space, width, height):
        self.collision_type = 0
        self.new_collision_type = 0
        self.static_lines = self.create_track(space, width, height, self.collision_type)
        self.new_static_lines = self.create_checkpoints(space, width, height, self.new_collision_type)
        self.height = height
        self.width = width

    @staticmethod
    def create_track(space, width, height, collision_type):
        set_track_width = 200
        track_width = set_track_width + 50
        if TRACK_CHOICE == 1:
            static_lines = [
                # Ramka zewnetrzna:
                pymunk.Segment(space.static_body, (50, 50), (50, height - 50), 5),
                pymunk.Segment(space.static_body, (50, height - 50), (width - 50, height - 50), 5),
                pymunk.Segment(space.static_body, (width - 50, height - 50), (width - 50, 50), 5),
                pymunk.Segment(space.static_body, (50, 50), (width - 50, 50), 5),

                # Ramka wewnetrzna:
                pymunk.Segment(space.static_body, (track_width, track_width), (track_width, height - track_width), 5),
                pymunk.Segment(space.static_body, (track_width, height - track_width),
                               (width - track_width, height - track_width), 5),
                pymunk.Segment(space.static_body, (width - track_width, height - track_width),
                               (width - track_width, track_width), 5),
                pymunk.Segment(space.static_body, (track_width, track_width), (width - track_width, track_width), 5),
            ]

        if TRACK_CHOICE == 2:
            static_lines = [

                # Ramka:
                pymunk.Segment(space.static_body, (50, height - 50), (50, 50), 5),
                pymunk.Segment(space.static_body, (50, height - 50), (width - 50, height - 50), 5),
                pymunk.Segment(space.static_body, (width - 50, height - 50), (width - 50, 50), 5),
                pymunk.Segment(space.static_body, (50, 50), (width - 50, 50), 5),

                # Przeszkody:
                pymunk.Segment(space.static_body, (200, height - 200), (200, 50), 5),
                pymunk.Segment(space.static_body, (400, height - 50), (400, 200), 5),
                pymunk.Segment(space.static_body, (600, height - 200), (600, 50), 5),
                pymunk.Segment(space.static_body, (800, height - 50), (800, 200), 5),
                pymunk.Segment(space.static_body, (1000, height - 200), (1000, 50), 5),
                pymunk.Segment(space.static_body, (1200, height - 50), (1200, 200), 5),
                pymunk.Segment(space.static_body, (1400, height - 200), (1400, 50), 5),
                pymunk.Segment(space.static_body, (1600, height - 50), (1600, 200), 5),
                pymunk.Segment(space.static_body, (1800, height - 200), (1800, 50), 5),
            ]

        for i, line in enumerate(static_lines):
            line.friction = 0
            line.color = (255, 0, 0)
            line.collision_type = collision_type
            space.add(line)

        return static_lines

    @staticmethod
    def create_checkpoints(space, width, height, collision_type):
        set_track_width = 200
        track_width = set_track_width + 50

        if TRACK_CHOICE == 1:
            static_lines = [

                # TOR 1
                # Linia START/META:
                pymunk.Segment(space.static_body, (width / 2, height - 50), (width / 2, height - track_width), 5),

                # Checkpoints:
                pymunk.Segment(space.static_body, (width - track_width, height / 2), (width - 50, height / 2), 5),
                pymunk.Segment(space.static_body, (50, height / 2), (track_width, height / 2), 5),
                pymunk.Segment(space.static_body, (width / 2, 50), (width / 2, track_width), 5)
            ]
        if TRACK_CHOICE == 2:
            static_lines = [
                # TOR 2

                # Linia META:
                pymunk.Segment(space.static_body, (width - 50, 50), (width - 50, 300), 5),

                # Checkpoints
                pymunk.Segment(space.static_body, (600, height - 50), (600, height - 200), 5),
                pymunk.Segment(space.static_body, (1000, height - 50), (1000, height - 200), 5),
                pymunk.Segment(space.static_body, (1400, height - 50), (1400, height - 200), 5),
            ]

        for i, line in enumerate(static_lines):
            line.friction = 0
            line.color = (0, 0, 255)
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
        for line in self.new_static_lines:
            body = line.body
            pv1 = body.position + line.a.rotated(body.angle)
            pv2 = body.position + line.b.rotated(body.angle)
            p1 = self.to_pygame(pv1)
            p2 = self.to_pygame(pv2)
            pygame.draw.lines(screen, line.color, False, [p1, p2])
