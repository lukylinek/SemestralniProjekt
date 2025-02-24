# timer_controls.py

import pygame
import sys
from variables import *

def show_time_selection_screen(window, width, height, font, BLACK, WHITE):
    window.fill(BLACK)
    
    text = font.render("Select Game Duration (seconds):", True, WHITE)
    text_rect = text.get_rect(center=(width // 2, height // 2 - 100))
    window.blit(text, text_rect)
    
    time_options = [15, 30, 45, 60]
    button_rects = []
    for i, time in enumerate(time_options):
        button_rect = pygame.Rect(width // 2 - 50, height // 2 - 25 + i * 60, 100, 50)
        pygame.draw.rect(window, WHITE, button_rect)
        button_text = font.render(str(time), True, BLACK)
        button_text_rect = button_text.get_rect(center=button_rect.center)
        window.blit(button_text, button_text_rect)
        button_rects.append((button_rect, time))
    
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button_rect, time in button_rects:
                    if button_rect.collidepoint(event.pos):
                        return time
    return None

def show_controls_screen(window, width, height, controls_screen_image, BLACK):
    zoomed_out_controls_image = pygame.transform.scale(controls_screen_image, (width // 4, height // 4))
    x_pos = 0
    y_pos = (height - zoomed_out_controls_image.get_height()) // 2
    
    window.fill(BLACK)
    window.blit(zoomed_out_controls_image, (x_pos, y_pos))
    pygame.display.flip()

def show_start_screen(window, width, height, start_screen_image, WHITE, BLACK):
    window.blit(start_screen_image, (0, 0))
    
    play_button_rect = pygame.Rect(width // 2 - 50, height // 2 - 25, 100, 50)
    pygame.draw.rect(window, WHITE, play_button_rect)
    font = pygame.font.Font(None, 36)
    text = font.render("Play", True, BLACK)
    text_rect = text.get_rect(center=play_button_rect.center)
    window.blit(text, text_rect)
    
    """
    controls_button_rect = pygame.Rect(width // 2 - 50, height // 2 + 50, 100, 50)
    pygame.draw.rect(window, WHITE, controls_button_rect)
    controls_text = font.render("Controls", True, BLACK)
    controls_text_rect = controls_text.get_rect(center=controls_button_rect.center)
    window.blit(controls_text, controls_text_rect)
    """
    
    time_button_rect = pygame.Rect(width // 2 - 50, height // 2 + 125, 100, 50)
    pygame.draw.rect(window, WHITE, time_button_rect)
    time_text = font.render("Time", True, BLACK)
    time_text_rect = time_text.get_rect(center=time_button_rect.center)
    window.blit(time_text, time_text_rect)
    
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    return "play"
                #elif controls_button_rect.collidepoint(event.pos):
                    return "controls"
                elif time_button_rect.collidepoint(event.pos):
                    return "time"
    return None

