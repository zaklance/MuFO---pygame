import pygame
from pygame.math import Vector2
from settings import scroll_thresh, SCREEN_WIDTH, SCREEN_HEIGHT, screen, scroll_thresh, screen_scroll, bg_scroll

def load_game_bg(image_path):
    return pygame.image.load(image_path)

def draw_game_bg(screen, game_bg, bg_scroll):
    screen.blit(game_bg, (bg_scroll[0], bg_scroll[1]))
    
def update_bg_scroll(bg_scroll, screen_scroll, bg_width, bg_height, screen_width, screen_height):
    if bg_scroll is None:
        bg_scroll = Vector2(0 ,0)  # Initialize bg_scroll if it's None

    if screen_scroll is not None:  # Ensure screen_scroll is not None
        bg_scroll -= screen_scroll
        
    max_scroll_x = 0
    min_scroll_x = -(bg_width - screen_width)
    max_scroll_y = 0
    min_scroll_y = -(bg_height - screen_height)
    
    bg_scroll.x = max(min_scroll_x, min(max_scroll_x, bg_scroll.x))
    bg_scroll.y = max(min_scroll_y, min(max_scroll_y, bg_scroll.y))

    return bg_scroll

class Building(pygame.sprite.Sprite):
    def __init__(self, building, x, y, flip = False):
        self.image = pygame.image.load(f'assets/img/buildings/{building}.png')
        if flip:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class House(Building):
    all_block = []
    def __init__(self, building, x, y, flip=False):
        super().__init__(building, x, y, flip)
        self.block = pygame.Rect(0, (self.image.get_height()-197), 153, 197)
        House.all_block.append(self.block)

class Watertower(Building):
    all_block = []
    def __init__(self, building, x, y, flip=False):
        super().__init__(building, x, y, flip)
        self.block = pygame.Rect(0, (self.image.get_height()-165), 252, 165)
        Watertower.all_block.append(self.block)
        
class Circus(Building):
    all_block = []
    def __init__(self, building, x, y, flip=False):
        super().__init__(building, x, y, flip)
        self.block = pygame.Rect(0, (self.image.get_height()-519), 687, 519)
        Circus.all_block.append(self.block)

class Grocery(Building):
    all_block = []
    def __init__(self, building, x, y, flip=False):
        super().__init__(building, x, y, flip)
        self.block = pygame.Rect(0, (self.image.get_height()-186), 343, 186)
        Grocery.all_block.append(self.block)

class Church(Building):
    all_block = []
    def __init__(self, building, x, y, flip=False):
        super().__init__(building, x, y, flip)
        self.block = pygame.Rect(0, (self.image.get_height()-229), 296, 229)
        Church.all_block.append(self.block)

class School(Building):
    all_block = []
    def __init__(self, building, x, y, flip=False):
        super().__init__(building, x, y, flip)
        self.block = pygame.Rect(0, (self.image.get_height()-569), 164, 569), pygame.Rect(379, 49, 190, 217)
        School.all_block.append(self.block)


