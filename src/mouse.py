import pygame

# Set resolution
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y, speed, max_range, y_offset=0):
        super().__init__()
        self.image = pygame.Surface((20, 5))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=(x, y + y_offset))  # Apply the y_offset here
        self.start_pos = pygame.math.Vector2(x, y + y_offset)
        self.target_pos = pygame.math.Vector2(target_x, target_y)
        self.speed = speed
        self.max_range = max_range
        self.direction = (self.target_pos - self.start_pos).normalize()
        self.distance_traveled = 0
        self.angle = self.direction.angle_to(pygame.math.Vector2(1, 0))
        self.image = pygame.transform.rotate(self.image, -self.angle)

    def update(self):
        movement = self.direction * self.speed
        self.rect.move_ip(movement)
        self.distance_traveled += self.speed
        if self.distance_traveled >= self.max_range:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class MouseControl:
    def __init__(self):
        self.crosshair_image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.crosshair_image, 'red', (10, 10), 10)  # Draw the circle on the surface
        self.click_sound = pygame.mixer.Sound('assets/sounds/effects/lazer.mp3')
        pygame.mouse.set_visible(False)  # Hide default mouse cursor

    def draw_crosshair(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        crosshair_rect = self.crosshair_image.get_rect(center=mouse_pos)
        screen.blit(self.crosshair_image, crosshair_rect)

    def handle_click(self):
        pygame.mouse.get_pressed()[0]

    def update(self, screen):
        self.draw_crosshair(screen)
        self.handle_click(player)
        self.lasers.update()
        for laser in self.lasers:
            laser.draw(screen)

    def process_events(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.draw_crosshair(screen)