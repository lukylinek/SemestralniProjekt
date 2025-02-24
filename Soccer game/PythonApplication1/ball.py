import pygame
from variables import *


class Ball:
    def __init__(self, frames, pos, velocity, speed, friction):
        self.frames = frames
        self.pos = pos
        self.velocity = velocity
        self.speed = speed
        self.friction = friction
        self.rect = pygame.Rect(pos[0], pos[1], 50, 50)
        self.frame_index = 0

    def move(self):
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
        self.velocity[0] *= self.friction
        self.velocity[1] *= self.friction
        if abs(self.velocity[0]) < 0.1:
            self.velocity[0] = 0
        if abs(self.velocity[1]) < 0.1:
            self.velocity[1] = 0
        self.rect.topleft = self.pos

        if self.pos[0] <= pitch_left:
            self.pos[0] = pitch_left
            self.velocity[0] = -self.velocity[0]
        if self.pos[0] >= pitch_right - 50:
            self.pos[0] = pitch_right - 50
            self.velocity[0] = -self.velocity[0]
        if self.pos[1] <= pitch_top:
            self.pos[1] = pitch_top
            self.velocity[1] = -self.velocity[1]
        if self.pos[1] >= pitch_bottom - 20:
            self.pos[1] = pitch_bottom - 20
            self.velocity[1] = -self.velocity[1]

    def draw(self, window):
        window.blit(self.frames[self.frame_index], self.pos)
        self.frame_index = (self.frame_index + 1) % len(self.frames)

