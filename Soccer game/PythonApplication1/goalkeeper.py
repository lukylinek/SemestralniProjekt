import pygame
from variables import *

class Goalkeeper:
    def __init__(self, image, pos, speed, top_limit, bottom_limit):
        self.image = image
        self.pos = pos
        self.speed = speed
        self.top_limit = top_limit
        self.bottom_limit = bottom_limit
        self.rect = pygame.Rect(pos[0], pos[1], 50, 50)

    def move(self, ball_pos):
        if ball_pos[1] < self.pos[1] and self.pos[1] > self.top_limit:
            self.pos[1] -= self.speed
        elif ball_pos[1] > self.pos[1] and self.pos[1] < self.bottom_limit:
            self.pos[1] += self.speed
        self.rect.topleft = self.pos

    def draw(self, window):
        window.blit(self.image, self.pos)

