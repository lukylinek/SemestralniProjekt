import pygame
import sys
from variables import *
from player import Player
from goalkeeper import Goalkeeper
from ball import Ball
from powerup import PowerUp
from playercls import check_goal, check_collision  
from timer_controls import show_time_selection_screen, show_controls_screen, show_start_screen  
 
 


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
        self.power_up_active = True
        self.power_up_start_time = None
        self.current_power_up_type, self.power_up_pos = self.power_up.spawn()

    def reset(self):
        self.player1.pos = initial_player1_pos[:]
        self.player2.pos = initial_player2_pos[:]
        self.goalkeeper1.pos = initial_goalkeeper1_pos[:]
        self.goalkeeper2.pos = initial_goalkeeper2_pos[:]
        self.ball.pos = [width // 2, height // 2]
        self.ball.velocity = [0, 0]
        self.start_ticks = pygame.time.get_ticks()

    def reset_positions(self):
        self.player1.pos = initial_player1_pos[:]
        self.player2.pos = initial_player2_pos[:]
        self.goalkeeper1.pos = initial_goalkeeper1_pos[:]
        self.goalkeeper2.pos = initial_goalkeeper2_pos[:]
        self.ball.pos = [width // 2, height // 2]
        self.ball.velocity = [0, 0]

    def update(self):
        keys = pygame.key.get_pressed()
        self.player1.move(keys, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pitch_top, pitch_bottom, pitch_left, pitch_right)
        self.player2.move(keys, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pitch_top, pitch_bottom, pitch_left, pitch_right)
        self.ball.move()
        self.goalkeeper1.move(self.ball.pos)
        self.goalkeeper2.move(self.ball.pos)
        self.check_collisions()
        self.check_power_up_collisions()

        
        seconds = (pygame.time.get_ticks() - self.start_ticks) / 1000
        self.remaining_time = max(0, self.game_time - int(seconds))

        
        if self.remaining_time <= 0:
            if self.score_team1 == self.score_team2:
                self.overtime = True
            else:
                self.running = False
                self.show_game_over_screen()

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
        check_collision(self.ball, self.player1, self.player2)

    def check_power_up_collisions(self):
        player1_rect = pygame.Rect(self.player1.pos[0], self.player1.pos[1], 50, 50)
        player2_rect = pygame.Rect(self.player2.pos[0], self.player2.pos[1], 50, 50)
        power_up_rect = pygame.Rect(self.power_up_pos[0], self.power_up_pos[1], 30, 30)

        if player1_rect.colliderect(power_up_rect) and self.power_up_active:
            self.power_up.apply(self.player1, self.current_power_up_type)
            self.power_up_active = False
            self.power_up_start_time = pygame.time.get_ticks()
        if player2_rect.colliderect(power_up_rect) and self.power_up_active:
            self.power_up.apply(self.player2, self.current_power_up_type)
            self.power_up_active = False
            self.power_up_start_time = pygame.time.get_ticks()

        if self.power_up_start_time and (pygame.time.get_ticks() - self.power_up_start_time) / 1000 >= self.power_up.durations[self.current_power_up_type]:
            self.power_up.reset(self.player1)
            self.power_up.reset(self.player2)
            self.power_up_start_time = None
            self.current_power_up_type, self.power_up_pos = self.power_up.spawn()
            self.power_up_active = True

    def draw(self):
        window.blit(pitch_image, (0, 0))
        self.player1.draw(window)
        self.player2.draw(window)
        self.ball.draw(window)
        self.goalkeeper1.draw(window)
        self.goalkeeper2.draw(window)
        if self.power_up_active:
            window.blit(self.power_up.image, self.power_up_pos)

        # Draw scores
        font = pygame.font.SysFont("Arial", 24)
        score_text_team1 = font.render(f"Barcelona: {self.score_team1}", True, (125, 0, 0))  # Red color
        score_text_team2 = font.render(f"Real Madrid: {self.score_team2}", True, WHITE)
        score_text_rect_team1 = score_text_team1.get_rect(center=(width // 2 - 150, 50))
        score_text_rect_team2 = score_text_team2.get_rect(center=(width // 2 + 150, 50))
        window.blit(score_text_team1, score_text_rect_team1)
        window.blit(score_text_team2, score_text_rect_team2)

        # Draw timer
        timer_text = font.render(f"Time: {self.remaining_time}", True, WHITE)
        timer_text_rect = timer_text.get_rect(center=(width // 2, 100))
        window.blit(timer_text, timer_text_rect)

        if self.overtime:
            overtime_text = font.render("Overtime", True, RED)
            overtime_text_rect = overtime_text.get_rect(center=(width // 2, height // 2))
            window.blit(overtime_text, overtime_text_rect)

    def show_game_over_screen(self):
        window.fill(BLACK)
        
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, WHITE)
        text_rect = text.get_rect(center=(width // 2, height // 2 - 50))
        window.blit(text, text_rect)
        
        font = pygame.font.Font(None, 36)
        score_text_team1 = font.render(f"Barcelona: {self.score_team1}", True, (125, 0, 0))  # Red color
        score_text_team2 = font.render(f"Real Madrid: {self.score_team2}", True, WHITE)
        score_text_rect_team1 = score_text_team1.get_rect(center=(width // 2, height // 2))
        score_text_rect_team2 = score_text_team2.get_rect(center=(width // 2, height // 2 + 50))
        window.blit(score_text_team1, score_text_rect_team1)
        window.blit(score_text_team2, score_text_rect_team2)
        
        restart_button_rect = pygame.Rect(width // 2 - 50, height // 2 + 100, 100, 50)
        pygame.draw.rect(window, WHITE, restart_button_rect)
        
        restart_text = font.render("Restart", True, BLACK)
        restart_text_rect = restart_text.get_rect(center=restart_button_rect.center)
        window.blit(restart_text, restart_text_rect)
        
        pygame.display.flip()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button_rect.collidepoint(event.pos):
                        waiting = False
                        self.reset()
                        self.run()

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.update()
            self.draw()
            pygame.display.flip()
            pygame.time.Clock().tick(60)

def main():
    pygame.init()
    font = pygame.font.Font(None, 36)
    action = show_start_screen(window, width, height, start_screen_image, WHITE, BLACK)
    if action == "play":
        game = Game()
        game.run()
    elif action == "time":
        game_time = show_time_selection_screen(window, width, height, font, BLACK, WHITE)
        if game_time:
            game = Game()
            game.game_time = game_time
            game.run()

if __name__ == "__main__":
    main()
