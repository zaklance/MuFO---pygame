import pygame
from pygame.math import Vector2

# Set resolution
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define scrolling variables
SCROLL_THRESH = SCREEN_WIDTH // 2
screen_scroll = Vector2(0, 0)
bg_scroll = Vector2(0, 0)

