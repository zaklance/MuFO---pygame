import pygame


def load_game_bg(image_path):
    return pygame.image.load(image_path)

def draw_game_bg(screen, game_bg, bg_scroll):
    screen.blit(game_bg, (bg_scroll[0], bg_scroll[1]))

def update_bg_scroll(bg_scroll, screen_scroll, bg_width, bg_height, screen_width, screen_height):
    bg_scroll[0] -= screen_scroll[0]
    bg_scroll[1] -= screen_scroll[1]

    bg_scroll[0] = max(-(bg_width - screen_width), min(0, bg_scroll[0]))
    bg_scroll[1] = max(-(bg_height - screen_height), min(0, bg_scroll[1]))

    return bg_scroll