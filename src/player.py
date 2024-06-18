import pygame
import os

# MAY GET DELETED

# Set resolution
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        self.alive = True
        self.load_images('idle', scale)
        self.flip = False
        self.image = self.animation_list[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.speed = speed

class Player_idle(Character):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

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
    
    def move(self, moving_left, moving_right, moving_up, moving_down, threshold_x, threshold_y):
        screen_scroll = [0, 0]
        dx = 0
        dy = 0

        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        if moving_up:
            dy = -self.speed
        if moving_down:
            dy = self.speed

        self.rect.x += dx
        self.rect.y += dy

        # Check horizontal threshold
        if self.rect.right > SCREEN_WIDTH - threshold_x:
            self.rect.right = SCREEN_WIDTH - threshold_x
            screen_scroll[0] = dx
        elif self.rect.left < threshold_x:
            self.rect.left = threshold_x
            screen_scroll[0] = dx

        # Check vertical threshold
        if self.rect.bottom > SCREEN_HEIGHT - threshold_y:
            self.rect.bottom = SCREEN_HEIGHT - threshold_y
            screen_scroll[1] = dy
        elif self.rect.top < threshold_y:
            self.rect.top = threshold_y
            screen_scroll[1] = dy

        return screen_scroll

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class Player_beam_down(Character):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)
        self.load_images('beam_down', scale)
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

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class Ufo(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        super().__init__()
        self.animation_list = []
        self.flip = False
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.speed = speed
        self.action = 0
        self.opacity = 255

        # Use the class name to determine the folder path
        class_name = self.__class__.__name__.lower()

        # Load images for target
        temp_list = []
        # Count number of files in the folder
        folder_path = f'assets/img/general/logo/{class_name}/'
        if not os.path.exists(folder_path):
            print(f"Error: Folder '{folder_path}' not found.")
            return  # Or handle the error as appropriate

        num_of_frames = len(os.listdir(folder_path))
        if num_of_frames == 0:
            print(f"Error: No frames found in '{folder_path}'.")
            return  # Or handle the error as appropriate

        for i in range(num_of_frames):
            img_path = os.path.join(folder_path, f'{i}.png')
            if not os.path.exists(img_path):
                print(f"Warning: File '{img_path}' not found.")
                continue  # Skip this frame and move to the next one

            img = pygame.image.load(img_path)
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            temp_list.append(img)

        if not temp_list:
            print(f"Error: No valid frames loaded for '{class_name}'.")
            return  # Or handle the error as appropriate

        self.animation_list.append(temp_list)

        self.image_orig = self.animation_list[0][-1]
        self.image = self.image_orig.copy()  
        
        self.rect = self.image.get_rect(topleft=(x, y))
        self.rect.center = (x, y)       

    def set_opacity(self, opacity):
        self.opacity = opacity

    def update(self):
        if pygame.time.get_ticks() - self.update_time > 100:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]

    def draw(self, screen):
        # Draw the target on the screen
        screen.blit(self.image, self.rect)

class Beam(Ufo):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Cow(Ufo):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

def main():
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 640
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Player Animation')

    clock = pygame.time.Clock()
    FPS = 6

    title_logo_scale = 2.5
    beam = Beam(400, 300, title_logo_scale, speed=5)
    ufo = Ufo(400, 300, title_logo_scale, speed=5)
    cow = Cow(400, 350, title_logo_scale, speed=5)

    beam.set_opacity(128)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill((0, 128, 0))
        beam.update()
        cow.update()
        ufo.update()

        beam.draw(screen)
        cow.draw(screen)
        ufo.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()

