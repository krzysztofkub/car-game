import random

import pygame

import cars_cache


class OptionsMenu:
    def __init__(self, game_setup):
        self.chart_button = Button(game_setup.width // 2, game_setup.height // 3, 200, 50, text='Draw chart')
        self.game_setup = game_setup
        self.overlay = pygame.Surface((self.game_setup.width, self.game_setup.height), pygame.SRCALPHA)
        self.is_active = False
        self.show_chart = False
        self.data_points = [(x, 1 * 1.6 ** x) for x in range(10)]

    def toggle(self):
        self.is_active = not self.is_active

    def draw(self):
        if self.show_chart:
            self.draw_chart()
        else:
            self.draw_option_menu()

    def draw_option_menu(self):
        self.overlay.fill((0, 0, 0, 128))
        self.game_setup.screen.blit(self.overlay, (0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render(f'Generation number: {cars_cache.cars_generation}', True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.game_setup.width // 2, self.game_setup.height // 4))

        button_font = pygame.font.Font(None, 36)
        self.chart_button.draw(self.game_setup.screen, button_font)

        self.game_setup.screen.blit(text, text_rect)

    def draw_chart(self):
        chart_height = 400
        chart_width = 600
        chart_x_start = (self.game_setup.width - chart_width) // 2
        chart_y_start = (self.game_setup.height - chart_height) // 2

        max_height = 100

        self.overlay.fill((0, 0, 0, 128))
        self.game_setup.screen.blit(self.overlay, (0, 0))

        font = pygame.font.Font(None, 30)
        axis_font = pygame.font.Font(None, 36)

        pygame.draw.rect(self.game_setup.screen, (30, 30, 30),
                         (chart_x_start, chart_y_start, chart_width, chart_height))

        for i in range(11):
            x = chart_x_start + i * (chart_width // 10)
            pygame.draw.line(self.game_setup.screen, (100, 100, 100), (x, chart_y_start),
                             (x, chart_y_start + chart_height))
            if i < 10:
                label = font.render(str(i * 10), True, (255, 255, 255))
                self.game_setup.screen.blit(label, (x, chart_y_start + chart_height + 10))

        for i in range(11):
            y = chart_y_start + i * (chart_height // 10)
            pygame.draw.line(self.game_setup.screen, (100, 100, 100), (chart_x_start, y),
                             (chart_x_start + chart_width, y))
            if i > 0:
                label = font.render(str(100 - i * 10), True, (255, 255, 255))
                self.game_setup.screen.blit(label, (chart_x_start - 40, y - 10))

        x_axis_name = "X-axis"
        y_axis_name = "Y-axis"
        x_label = axis_font.render(x_axis_name, True, (255, 255, 255))
        y_label = axis_font.render(y_axis_name, True, (255, 255, 255))
        self.game_setup.screen.blit(x_label, (
        chart_x_start + chart_width // 2 - x_label.get_width() // 2, chart_y_start + chart_height + 30))
        self.game_setup.screen.blit(y_label, (chart_x_start - 60, chart_y_start - 30))

        prev_point = None
        for (x, y) in self.data_points:
            scaled_x = chart_x_start + int((x / max(self.data_points, key=lambda item: item[0])[0]) * chart_width)
            scaled_y = chart_y_start + chart_height - int((y / max_height) * chart_height)
            if prev_point:
                pygame.draw.line(self.game_setup.screen, (0, 255, 0), prev_point, (scaled_x, scaled_y), 2)
            pygame.draw.circle(self.game_setup.screen, (255, 0, 0), (scaled_x, scaled_y), 5)
            prev_point = (scaled_x, scaled_y)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.chart_button.is_over(pos):
                self.show_chart = not self.show_chart
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.show_chart = False


class Button:
    def __init__(self, x, y, width, height, text='', color=(73, 73, 73), text_color=(255, 255, 255)):
        self.center_x = x
        self.center_y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.text_color = text_color

    def draw(self, screen, font):
        top_left_x = self.center_x - self.width // 2
        top_left_y = self.center_y - self.height // 2

        pygame.draw.rect(screen, self.color, (top_left_x, top_left_y, self.width, self.height))

        if self.text != '':
            text_surface = font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=(self.center_x, self.center_y))
            screen.blit(text_surface, text_rect)

    def is_over(self, pos):
        if self.center_x - self.width // 2 < pos[0] < self.center_x + self.width // 2 and \
                self.center_y - self.height // 2 < pos[1] < self.center_y + self.height // 2:
            return True
        return False
