import pygame
from variables import *

def check_goal(ball_pos, pitch_left, pitch_right, goal_top, goal_bottom):
    if ball_pos[0] <= pitch_left and goal_top <= ball_pos[1] <= goal_bottom:
        return "team2"
    elif ball_pos[0] >= pitch_right - 50 and goal_top <= ball_pos[1] <= goal_bottom:
        return "team1"
    return None

def check_collision(ball, player1, player2):
    ball_rect = pygame.Rect(ball.pos[0], ball.pos[1], 50, 50)
    player1_rect = pygame.Rect(player1.pos[0], player1.pos[1], 50, 50)
    player2_rect = pygame.Rect(player2.pos[0], player2.pos[1], 50, 50)

    if player1_rect.colliderect(ball_rect):
        if player1.pos[1] < ball.pos[1]:
            ball.velocity[1] = ball.speed + player1.speed
        else:
            ball.velocity[1] = -ball.speed - player1.speed
        if player1.pos[0] < ball.pos[0]:
            ball.velocity[0] = ball.speed + player1.speed
        else:
            ball.velocity[0] = -ball.speed - player1.speed

    if player2_rect.colliderect(ball_rect):
        if player2.pos[1] < ball.pos[1]:
            ball.velocity[1] = ball.speed + player2.speed
        else:
            ball.velocity[1] = -ball.speed - player2.speed
        if player2.pos[0] < ball.pos[0]:
            ball.velocity[0] = ball.speed + player2.speed
        else:
            ball.velocity[0] = -ball.speed - player2.speed
