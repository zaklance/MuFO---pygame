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

def update_bg_scroll(bg_scroll, screen_scroll, bg_width, bg_height, screen_width, screen_height):
    if bg_scroll is None:
        bg_scroll = [0, 0]  # Initialize bg_scroll if it's None

    if screen_scroll is not None:  # Ensure screen_scroll is not None
        bg_scroll[0] -= screen_scroll[0]
        bg_scroll[1] -= screen_scroll[1]

    bg_scroll[0] = max(-(bg_width - screen_width), min(0, bg_scroll[0]))
    bg_scroll[1] = max(-(bg_height - screen_height), min(0, bg_scroll[1]))

    return bg_scroll