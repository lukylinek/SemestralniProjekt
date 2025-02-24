import pygame
from variables import *

class Player:
    def __init__(self, image, pos, speed):
        self.image = image
        self.pos = pos
        self.speed = speed
        self.rect = pygame.Rect(pos[0], pos[1], 50, 50)

    def move(self, keys, up, down, left, right, pitch_top, pitch_bottom, pitch_left, pitch_right):
        if keys[up] and self.pos[1] > pitch_top - 20:
            self.pos[1] -= self.speed
        if keys[down] and self.pos[1] < pitch_bottom - 30:
            self.pos[1] += self.speed
        if keys[left] and self.pos[0] > pitch_left - 20:
            self.pos[0] -= self.speed
        if keys[right] and self.pos[0] < pitch_right - 30:
            self.pos[0] += self.speed
        self.rect.topleft = self.pos

    def draw(self, window):
        window.blit(self.image, self.pos)

