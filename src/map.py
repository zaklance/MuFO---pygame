import pygame


def load_game_bg(image_path):
    return pygame.image.load(image_path)

def draw_game_bg(screen, game_bg, bg_scroll):
    screen.blit(game_bg, (bg_scroll[0], bg_scroll[1]))

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


def update_bg_scroll(bg_scroll, screen_scroll, bg_width, bg_height, screen_width, screen_height):
    if bg_scroll is None:
        bg_scroll = [0, 0]  # Initialize bg_scroll if it's None

    if screen_scroll is not None:  # Ensure screen_scroll is not None
        bg_scroll[0] -= screen_scroll[0]
        bg_scroll[1] -= screen_scroll[1]

    bg_scroll[0] = max(-(bg_width - screen_width), min(0, bg_scroll[0]))
    bg_scroll[1] = max(-(bg_height - screen_height), min(0, bg_scroll[1]))

    return bg_scroll