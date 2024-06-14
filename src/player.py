import pygame
import os

class PlayerIdle(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        super().__init__()
        self.load_images('idle', scale)
        self.image = self.animation_list[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def load_images(self, action, scale):
        self.animation_list = []
        folder_path = f'assets/img/player/{action}/'
        num_of_frames = len(os.listdir(folder_path))
        for i in range(num_of_frames):
            img_path = os.path.join(folder_path, f'{i}.png')
            img = pygame.image.load(img_path)
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.animation_list.append(img)

    def update(self):
        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > 100:
            self.update_time = pygame.time.get_ticks()
            self.frame_index = (self.frame_index + 1) % len(self.animation_list)

class PlayerBeamDown(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        super().__init__()
        self.load_images('beam_down', scale)
        self.image = self.animation_list[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.is_beam_active = False
        self.reverse = False
        self.spacebar_held = False

    def load_images(self, action, scale):
        self.animation_list = []
        folder_path = f'assets/img/player/{action}/'
        num_of_frames = len(os.listdir(folder_path))
        for i in range(num_of_frames):
            img_path = os.path.join(folder_path, f'{i}.png')
            img = pygame.image.load(img_path)
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.animation_list.append(img)

    def start_beam(self):
        self.is_beam_active = True
        self.reverse = False

    def end_beam(self):
        self.reverse = True

    def update(self):
        if self.is_beam_active:
            self.image = self.animation_list[self.frame_index]
            if pygame.time.get_ticks() - self.update_time > 100:
                self.update_time = pygame.time.get_ticks()
                if not self.reverse:
                    if self.frame_index < len(self.animation_list) - 1:
                        self.frame_index += 1
                else:
                    if self.frame_index > 0:
                        self.frame_index -= 1
                    else:
                        self.is_beam_active = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.spacebar_held = True
            if not self.is_beam_active:
                self.start_beam()
        elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            self.spacebar_held = False
            self.end_beam()

def main():
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 640
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Player Animation')

    clock = pygame.time.Clock()
    FPS = 6

    player_scale = 2.5
    player_idle = PlayerIdle(400, 400, player_scale)
    player_beam_down = PlayerBeamDown(400, 400, player_scale)

    all_sprites = pygame.sprite.LayeredUpdates()
    all_sprites.add(player_beam_down, layer=0)
    all_sprites.add(player_idle, layer=1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            player_beam_down.handle_event(event)

        screen.fill((0, 128, 0))
        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()

