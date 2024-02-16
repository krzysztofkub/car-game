import pygame
import pymunk
from pymunk import pygame_util

import constants
from constants import TRACK_CHOICE


class Track:
    checkpoints_number = 0

    def __init__(self, space, width, height):
        self.collision_type = constants.TRACK_COLLISION_TYPE
        self.static_lines = self.create_track(space, width, height)
        self.checkpoints = self.create_checkpoints(space, width, height)
        self.height = height
        self.width = width

    def create_track(self, space, width, height):
        set_track_width = 200
        track_width = set_track_width + 50
        if TRACK_CHOICE == 1:
            static_lines = [
                # Boarder:
                pymunk.Segment(space.static_body, (50, 50), (50, height - 50), 5),
                pymunk.Segment(space.static_body, (50, height - 50), (width - 50, height - 50), 5),
                pymunk.Segment(space.static_body, (width - 50, height - 50), (width - 50, 50), 5),
                pymunk.Segment(space.static_body, (50, 50), (width - 50, 50), 5),

                # Track:
                pymunk.Segment(space.static_body, (track_width, track_width), (track_width, height - track_width), 5),
                pymunk.Segment(space.static_body, (track_width, height - track_width),
                               (width - track_width, height - track_width), 5),
                pymunk.Segment(space.static_body, (width - track_width, height - track_width),
                               (width - track_width, track_width), 5),
                pymunk.Segment(space.static_body, (track_width, track_width), (width - track_width, track_width), 5),
            ]

        if TRACK_CHOICE == 2:
            static_lines = [

                # Boarder:
                pymunk.Segment(space.static_body, (50, height - 50), (50, 50), 5),
                pymunk.Segment(space.static_body, (50, height - 50), (width - 50, height - 50), 5),
                pymunk.Segment(space.static_body, (width - 50, height - 50), (width - 50, 50), 5),
                pymunk.Segment(space.static_body, (50, 50), (width - 50, 50), 5),

                # Track:
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
            line.collision_type = self.collision_type
            space.add(line)

        return static_lines

    @staticmethod
    def create_checkpoints(space, width, height):
        set_track_width = 200
        track_width = set_track_width + 50

        if TRACK_CHOICE == 1:
            static_lines = [

                # TRACK 1
                # FINISH LINE:
                pymunk.Segment(space.static_body, (width / 2, height - 50), (width / 2, height - track_width), 5),

                # Checkpoints:
                pymunk.Segment(space.static_body, (width - track_width, height / 2), (width - 50, height / 2), 5),
                pymunk.Segment(space.static_body, (50, height / 2), (track_width, height / 2), 5),
                pymunk.Segment(space.static_body, (width / 2, 50), (width / 2, track_width), 5)
            ]
        if TRACK_CHOICE == 2:
            static_lines = [

                # TRACK 2
                pymunk.Segment(space.static_body, (width - 50, 50), (width - 50, 300), 5),

                pymunk.Segment(space.static_body, (200, height - 50), (200, height - 200), 5),
                pymunk.Segment(space.static_body, (200, height - 200), (50, height - 50), 5),

                pymunk.Segment(space.static_body, (200, height - 200), (50, height - 200), 5),
                pymunk.Segment(space.static_body, (200, height - 300), (50, height - 300), 5),
                pymunk.Segment(space.static_body, (200, height - 400), (50, height - 400), 5),
                pymunk.Segment(space.static_body, (200, height - 500), (50, height - 500), 5),
                pymunk.Segment(space.static_body, (200, height - 600), (50, height - 600), 5),
                pymunk.Segment(space.static_body, (200, height - 700), (50, height - 700), 5),

                pymunk.Segment(space.static_body, (200, height - 200), (400, height - 200), 5),
                pymunk.Segment(space.static_body, (200, height - 300), (400, height - 300), 5),
                pymunk.Segment(space.static_body, (200, height - 400), (400, height - 400), 5),
                pymunk.Segment(space.static_body, (200, height - 500), (400, height - 500), 5),
                pymunk.Segment(space.static_body, (200, height - 600), (400, height - 600), 5),
                pymunk.Segment(space.static_body, (200, height - 700), (400, height - 700), 5),
                pymunk.Segment(space.static_body, (200, height - 200), (400, height - 50), 5),

                pymunk.Segment(space.static_body, (400, 200), (200, 200), 5),
                pymunk.Segment(space.static_body, (400, 200), (200, 50), 5),
                pymunk.Segment(space.static_body, (400, 200), (400, 50), 5),
                pymunk.Segment(space.static_body, (400, 200), (600, 50), 5),
                pymunk.Segment(space.static_body, (400, 200), (600, 200), 5),

                pymunk.Segment(space.static_body, (600, height - 50), (600, height - 200), 5),
                pymunk.Segment(space.static_body, (600, height - 200), (400, height - 50), 5),
                pymunk.Segment(space.static_body, (600, height - 200), (400, height - 200), 5),
                pymunk.Segment(space.static_body, (600, height - 300), (400, height - 300), 5),
                pymunk.Segment(space.static_body, (600, height - 400), (400, height - 400), 5),
                pymunk.Segment(space.static_body, (600, height - 500), (400, height - 500), 5),
                pymunk.Segment(space.static_body, (600, height - 600), (400, height - 600), 5),
                pymunk.Segment(space.static_body, (600, height - 700), (400, height - 700), 5),
                pymunk.Segment(space.static_body, (600, height - 200), (800, height - 50), 5),
                pymunk.Segment(space.static_body, (600, height - 200), (800, height - 200), 5),

                pymunk.Segment(space.static_body, (800, 200), (600, 200), 5),
                pymunk.Segment(space.static_body, (800, 300), (600, 300), 5),
                pymunk.Segment(space.static_body, (800, 400), (600, 400), 5),
                pymunk.Segment(space.static_body, (800, 500), (600, 500), 5),
                pymunk.Segment(space.static_body, (800, 600), (600, 600), 5),
                pymunk.Segment(space.static_body, (800, 700), (600, 700), 5),
                pymunk.Segment(space.static_body, (800, 200), (600, 50), 5),
                pymunk.Segment(space.static_body, (800, 200), (800, 50), 5),
                pymunk.Segment(space.static_body, (800, 200), (1000, 50), 5),
                pymunk.Segment(space.static_body, (800, 200), (1000, 200), 5),

                pymunk.Segment(space.static_body, (1000, height - 50), (1000, height - 200), 5),
                pymunk.Segment(space.static_body, (1000, height - 200), (800, height - 50), 5),
                pymunk.Segment(space.static_body, (1000, height - 200), (800, height - 200), 5),
                pymunk.Segment(space.static_body, (1000, height - 300), (800, height - 300), 5),
                pymunk.Segment(space.static_body, (1000, height - 400), (800, height - 400), 5),
                pymunk.Segment(space.static_body, (1000, height - 500), (800, height - 500), 5),
                pymunk.Segment(space.static_body, (1000, height - 600), (800, height - 600), 5),
                pymunk.Segment(space.static_body, (1000, height - 700), (800, height - 700), 5),
                pymunk.Segment(space.static_body, (1000, height - 200), (1200, height - 50), 5),
                pymunk.Segment(space.static_body, (1000, height - 200), (1200, height - 200), 5),

                pymunk.Segment(space.static_body, (1200, 200), (1000, 200), 5),
                pymunk.Segment(space.static_body, (1200, 300), (1000, 300), 5),
                pymunk.Segment(space.static_body, (1200, 400), (1000, 400), 5),
                pymunk.Segment(space.static_body, (1200, 500), (1000, 500), 5),
                pymunk.Segment(space.static_body, (1200, 600), (1000, 600), 5),
                pymunk.Segment(space.static_body, (1200, 700), (1000, 700), 5),
                pymunk.Segment(space.static_body, (1200, 200), (1000, 50), 5),
                pymunk.Segment(space.static_body, (1200, 200), (1200, 50), 5),
                pymunk.Segment(space.static_body, (1200, 200), (1400, 50), 5),
                pymunk.Segment(space.static_body, (1200, 200), (1400, 200), 5),

                pymunk.Segment(space.static_body, (1400, height - 50), (1400, height - 200), 5),
                pymunk.Segment(space.static_body, (1400, height - 200), (1200, height - 50), 5),
                pymunk.Segment(space.static_body, (1400, height - 200), (1200, height - 200), 5),
                pymunk.Segment(space.static_body, (1400, height - 300), (1200, height - 300), 5),
                pymunk.Segment(space.static_body, (1400, height - 400), (1200, height - 400), 5),
                pymunk.Segment(space.static_body, (1400, height - 500), (1200, height - 500), 5),
                pymunk.Segment(space.static_body, (1400, height - 600), (1200, height - 600), 5),
                pymunk.Segment(space.static_body, (1400, height - 700), (1200, height - 700), 5),
                pymunk.Segment(space.static_body, (1400, height - 200), (1600, height - 50), 5),
                pymunk.Segment(space.static_body, (1400, height - 200), (1600, height - 200), 5),

                pymunk.Segment(space.static_body, (1600, 200), (1400, 200), 5),
                pymunk.Segment(space.static_body, (1600, 300), (1400, 300), 5),
                pymunk.Segment(space.static_body, (1600, 400), (1400, 400), 5),
                pymunk.Segment(space.static_body, (1600, 500), (1400, 500), 5),
                pymunk.Segment(space.static_body, (1600, 600), (1400, 600), 5),
                pymunk.Segment(space.static_body, (1600, 700), (1400, 700), 5),
                pymunk.Segment(space.static_body, (1600, 200), (1400, 50), 5),
                pymunk.Segment(space.static_body, (1600, 200), (1600, 50), 5),
                pymunk.Segment(space.static_body, (1600, 200), (1800, 50), 5),
                pymunk.Segment(space.static_body, (1600, 200), (1800, 200), 5),

                pymunk.Segment(space.static_body, (1800, height - 50), (1800, height - 200), 5),
                pymunk.Segment(space.static_body, (1800, height - 200), (1600, height - 50), 5),
                pymunk.Segment(space.static_body, (1800, height - 200), (1600, height - 200), 5),
                pymunk.Segment(space.static_body, (1800, height - 300), (1600, height - 300), 5),
                pymunk.Segment(space.static_body, (1800, height - 400), (1600, height - 400), 5),
                pymunk.Segment(space.static_body, (1800, height - 500), (1600, height - 500), 5),
                pymunk.Segment(space.static_body, (1800, height - 600), (1600, height - 600), 5),
                pymunk.Segment(space.static_body, (1800, height - 700), (1600, height - 700), 5),
                pymunk.Segment(space.static_body, (1800, height - 200), (1950, height - 50), 5),
                pymunk.Segment(space.static_body, (1800, height - 200), (1950, height - 200), 5),
                pymunk.Segment(space.static_body, (1800, height - 300), (1950, height - 300), 5),
                pymunk.Segment(space.static_body, (1800, height - 400), (1950, height - 400), 5),
                pymunk.Segment(space.static_body, (1800, height - 500), (1950, height - 500), 5),
                pymunk.Segment(space.static_body, (1800, height - 600), (1950, height - 600), 5),

            ]

        for i, line in enumerate(static_lines):
            line.friction = 0
            line.color = (0, 0, 255)
            line.collision_type = constants.CHECKPOINT_COLLISION_TYPE
            line.checkpoint_id = i
            space.add(line)

        Track.checkpoints_number = len(static_lines)
        return static_lines

    @staticmethod
    def get_checkpoints_number():
        return Track.checkpoints_number

    def draw(self, screen):
        for line in self.static_lines:
            body = line.body
            pv1 = body.position + line.a.rotated(body.angle)
            pv2 = body.position + line.b.rotated(body.angle)
            p1 = pygame_util.to_pygame(pv1, screen)
            p2 = pygame_util.to_pygame(pv2, screen)
            pygame.draw.lines(screen, line.color, False, [p1, p2])
        if constants.DRAW_CHECKPOINTS:
            for line in self.checkpoints:
                body = line.body
                pv1 = body.position + line.a.rotated(body.angle)
                pv2 = body.position + line.b.rotated(body.angle)
                p1 = pygame_util.to_pygame(pv1, screen)
                p2 = pygame_util.to_pygame(pv2, screen)
                pygame.draw.lines(screen, line.color, False, [p1, p2])
