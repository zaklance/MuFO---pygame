import pygame

# Set resolution
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class MouseControl:
    def __init__(self):
        self.crosshair_image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.crosshair_image, 'red', (10, 10), 10)  # Draw the circle on the surface
        self.click_sound = pygame.mixer.Sound('assets/sounds/effects/lazer.mp3')
        pygame.mouse.set_visible(False)  # Hide default mouse cursor

    def draw_crosshair(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        crosshair_rect = self.crosshair_image.get_rect(center = mouse_pos)
        screen.blit(self.crosshair_image, crosshair_rect)

    def handle_click(self):
        pygame.mouse.get_pressed()[0]

    def update(self, screen):
        self.draw_crosshair(screen)
        self.handle_click()

    def process_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                self.click_sound.play()
        elif event.type == pygame.MOUSEMOTION:
            self.draw_crosshair(screen)