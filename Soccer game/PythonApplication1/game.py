import pygame
import sys
from variables import *
from player import Player
from goalkeeper import Goalkeeper
from ball import Ball
from powerup import PowerUp

class Game:
    def __init__(self):
        self.goal_top = height // 2 - 50
        self.goal_bottom = height // 2 + 50
        self.player1 = Player(player1_image, initial_player1_pos[:], player1_speed)
        self.player2 = Player(player2_image, initial_player2_pos[:], player2_speed)
        self.goalkeeper1 = Goalkeeper(goalkeeper1_image, initial_goalkeeper1_pos[:], goalkeeper_speed, goalkeeper1_top, goalkeeper1_bottom)
        self.goalkeeper2 = Goalkeeper(goalkeeper2_image, initial_goalkeeper2_pos[:], goalkeeper_speed, goalkeeper2_top, goalkeeper2_bottom)
        self.ball = Ball(soccer_ball_frames, soccer_ball_pos[:], soccer_ball_velocity[:], ball_speed, friction)
        self.power_up = PowerUp(power_up_image, POWER_UP_TYPES, POWER_UP_DURATIONS)
        self.score_team1 = 0
        self.score_team2 = 0
        self.start_ticks = pygame.time.get_ticks()
        self.game_time = game_time
        self.overtime = False

    def reset(self):
        self.player1.pos = initial_player1_pos[:]
        self.player2.pos = initial_player2_pos[:]
        self.goalkeeper1.pos = initial_goalkeeper1_pos[:]
        self.goalkeeper2.pos = initial_goalkeeper2_pos[:]
        self.ball.pos = [width // 2, height // 2]
        self.ball.velocity = [0, 0]
        self.score_team1 = 0
        self.score_team2 = 0
        self.start_ticks = pygame.time.get_ticks()

    def update(self):
        keys = pygame.key.get_pressed()
        self.player1.move(keys, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pitch_top, pitch_bottom, pitch_left, pitch_right)
        self.player2.move(keys, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pitch_top, pitch_bottom, pitch_left, pitch_right)
        self.ball.move()
        self.goalkeeper1.move(self.ball.pos)
        self.goalkeeper2.move(self.ball.pos)

        # Check for collisions and goals
        
    def check_collisions(self):
        goal_scored = check_goal(self.ball.pos, pitch_left, pitch_right, self.goal_top, self.goal_bottom)
        if goal_scored == "team2":
            self.score_team2 += 1
            if self.overtime:
                self.running = False
                self.show_game_over_screen()
                return
            self.reset_positions()
        elif goal_scored == "team1":
            self.score_team1 += 1
            if self.overtime:
                self.running = False
                self.show_game_over_screen()
                return
            self.reset_positions()
    def draw(self):
        window.blit(pitch_image, (0, 0))
        self.player1.draw(window)
        self.player2.draw(window)
        self.ball.draw(window)
        self.goalkeeper1.draw(window)
        self.goalkeeper2.draw(window)
        self.power_up.draw(window)

        # Draw scores and timer
        

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.update()
            self.draw()
            pygame.display.flip()
            pygame.time.Clock().tick(60)

def show_start_screen():
    window.blit(start_screen_image, (0, 0))
    play_button_rect = pygame.Rect(width // 2 - 50, height // 2 - 25, 100, 50)
    pygame.draw.rect(window, WHITE, play_button_rect)
    font = pygame.font.Font(None, 36)
    text = font.render("Play", True, BLACK)
    text_rect = text.get_rect(center=play_button_rect.center)
    window.blit(text, text_rect)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    waiting = False

def main():
    show_start_screen()
    game = Game()
    game.run()

if __name__ == "__main__":
    main()

