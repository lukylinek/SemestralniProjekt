import pygame
import random
from variables import *

class PowerUp:
    def __init__(self, image, types, durations):
        self.image = image
        self.types = types
        self.durations = durations
        self.type, self.pos = self.spawn()
        self.active = True
        self.start_time = None
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 30, 30)

    def spawn(self):
        power_up_type = random.choice(self.types)
        power_up_pos = [random.randint(pitch_left, pitch_right - 30), random.randint(pitch_top, pitch_bottom - 30)]
        return power_up_type, power_up_pos

    def apply(self, player , power_up_type):
        if self.type == "speed_boost":
            player.speed *= 2

    def reset(self, player):
        if self.type == "speed_boost":
            player.speed /= 2

    def draw(self, window):
        if self.active:
            window.blit(self.image, self.pos)

