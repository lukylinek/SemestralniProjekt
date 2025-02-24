import pygame
import random
import sys
from PIL import Image

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Soccer Game")

start_screen_image = pygame.image.load("hra.png")
start_screen_image = pygame.transform.scale(start_screen_image, (width, height))

controls_screen_image = pygame.image.load('controls.jpg')

pitch_image = pygame.image.load("pitch.png")
pitch_image = pygame.transform.scale(pitch_image, (width, height))

player1_image = pygame.image.load("player_1.png")
player1_image = pygame.transform.scale(player1_image, (50, 50))
player2_image = pygame.image.load("player_2.png")
player2_image = pygame.transform.scale(player2_image, (50, 50))

goalkeeper1_image = pygame.image.load("player_1.png")
goalkeeper1_image = pygame.transform.scale(goalkeeper1_image, (50, 50))
goalkeeper2_image = pygame.image.load("player_2.png")
goalkeeper2_image = pygame.transform.scale(goalkeeper2_image, (50, 50))

soccer_ball_gif = Image.open("soccer_ball.gif")
soccer_ball_frames = []
for frame in range(soccer_ball_gif.n_frames):
    soccer_ball_gif.seek(frame)
    frame_image = soccer_ball_gif.convert("RGBA")
    frame_surface = pygame.image.fromstring(frame_image.tobytes(), frame_image.size, frame_image.mode)
    soccer_ball_frames.append(frame_surface)

power_up_image = pygame.image.load("power_up.png")
power_up_image = pygame.transform.scale(power_up_image, (30, 30))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

initial_player1_pos = [100, height // 2]
initial_player2_pos = [width - 150, height // 2]
player1_pos = initial_player1_pos[:]
player2_pos = initial_player2_pos[:]
soccer_ball_pos = [width // 2, height // 2]
soccer_ball_velocity = [0, 0]

player1_speed = 3.5
player2_speed = 3.5

ball_speed = 3
friction = 0.9

pitch_left = 30
pitch_right = width - 30
pitch_top = 30
pitch_bottom = height - 10

initial_goalkeeper1_pos = [pitch_left - 20, height // 2]
initial_goalkeeper2_pos = [pitch_right - 20, height // 2]
goalkeeper1_pos = initial_goalkeeper1_pos[:]
goalkeeper2_pos = initial_goalkeeper2_pos[:]

goalkeeper_speed = 1
goalkeeper1_direction = 1
goalkeeper2_direction = 1

goalkeeper1_top = initial_goalkeeper1_pos[1] - 60
goalkeeper1_bottom = initial_goalkeeper1_pos[1] + 30
goalkeeper2_top = initial_goalkeeper2_pos[1] - 60
goalkeeper2_bottom = initial_goalkeeper2_pos[1] + 30

POWER_UP_TYPES = ["speed_boost"]

POWER_UP_DURATIONS = {
    "speed_boost": 10
}

current_power_up_type, power_up_pos = random.choice(POWER_UP_TYPES), [random.randint(pitch_left, pitch_right - 30), random.randint(pitch_top, pitch_bottom - 30)]
power_up_active = True

score_team1 = 0
score_team2 = 0

game_time = 60
start_ticks = pygame.time.get_ticks()

player1_image_up = pygame.image.load("player_1_up.png")
player1_image_up = pygame.transform.scale(player1_image_up, (50, 50))
player1_image_down = pygame.image.load("player_1_down.png")
player1_image_down = pygame.transform.scale(player1_image_down, (50, 50))
player1_image_left = pygame.image.load("player_1_left.png")
player1_image_left = pygame.transform.scale(player1_image_left, (50, 50))
player1_image_right = pygame.image.load("player_1.png")
player1_image_right = pygame.transform.scale(player1_image_right, (50, 50))

player2_image_up = pygame.image.load("player_2_up.png")
player2_image_up = pygame.transform.scale(player2_image_up, (50, 50))
player2_image_down = pygame.image.load("player_2_down.png")
player2_image_down = pygame.transform.scale(player2_image_down, (50, 50))
player2_image_left = pygame.image.load("player_2.png")
player2_image_left = pygame.transform.scale(player2_image_left, (50, 50))
player2_image_right = pygame.image.load("player_2 _right.png")
player2_image_right = pygame.transform.scale(player2_image_right, (50, 50))

