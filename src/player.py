import pygame
import os

class Player_moving(pygame.sprite.Sprite):

    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        # Load images for target
        temp_list = []
        # Count number of files in the folder
        folder_path = f'assets/img/player/moving/'
        if not os.path.exists(folder_path):
            print(f"Error: Folder '{folder_path}' not found.")
            return  # Or handle the error as appropriate

        num_of_frames = len(os.listdir(folder_path))
        for i in range(num_of_frames):
            img_path = os.path.join(folder_path, f'{i}.png')
            if not os.path.exists(img_path):
                print(f"Warning: File '{img_path}' not found.")
                continue  # Skip this frame and move to the next one

            img = pygame.image.load(img_path)
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            temp_list.append(img)

        self.animation_list.append(temp_list)
        
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        # Update animation frames
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > 100:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0

    def draw(self, screen):
        # Draw the target on the screen
        screen.blit(self.image, self.rect)

class Player_idle(pygame.sprite.Sprite):

    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        # Load images for target
        temp_list = []
        # Count number of files in the folder
        folder_path = f'assets/img/player/idle/'
        if not os.path.exists(folder_path):
            print(f"Error: Folder '{folder_path}' not found.")
            return  # Or handle the error as appropriate

        num_of_frames = len(os.listdir(folder_path))
        for i in range(num_of_frames):
            img_path = os.path.join(folder_path, f'{i}.png')
            if not os.path.exists(img_path):
                print(f"Warning: File '{img_path}' not found.")
                continue  # Skip this frame and move to the next one

            img = pygame.image.load(img_path)
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            temp_list.append(img)

        self.animation_list.append(temp_list)
        
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def update(self):
        # Update animation frames
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > 100:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0

    def draw(self, screen):
        # Draw the target on the screen
        screen.blit(self.image, self.rect)

class Player_beam_up(pygame.sprite.Sprite):

    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        # Load images for target
        temp_list = []
        # Count number of files in the folder
        folder_path = f'assets/img/player/beam_up/'
        if not os.path.exists(folder_path):
            print(f"Error: Folder '{folder_path}' not found.")
            return  # Or handle the error as appropriate

        num_of_frames = len(os.listdir(folder_path))
        for i in range(num_of_frames):
            img_path = os.path.join(folder_path, f'{i}.png')
            if not os.path.exists(img_path):
                print(f"Warning: File '{img_path}' not found.")
                continue  # Skip this frame and move to the next one

            img = pygame.image.load(img_path)
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            temp_list.append(img)

        self.animation_list.append(temp_list)
        
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def update(self):
        # Update animation frames
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > 100:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0

    def draw(self, screen):
        # Draw the target on the screen
        screen.blit(self.image, self.rect)
        
class Player_beam_down(pygame.sprite.Sprite):

    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        # Load images for target
        temp_list = []
        # Count number of files in the folder
        folder_path = f'assets/img/player/beam_down/'
        if not os.path.exists(folder_path):
            print(f"Error: Folder '{folder_path}' not found.")
            return  # Or handle the error as appropriate

        num_of_frames = len(os.listdir(folder_path))
        for i in range(num_of_frames):
            img_path = os.path.join(folder_path, f'{i}.png')
            if not os.path.exists(img_path):
                print(f"Warning: File '{img_path}' not found.")
                continue  # Skip this frame and move to the next one

            img = pygame.image.load(img_path)
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            temp_list.append(img)

        self.animation_list.append(temp_list)
        
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def update(self):
        # Update animation frames
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > 100:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0

    def draw(self, screen):
        # Draw the target on the screen
        screen.blit(self.image, self.rect)

class Player_beam(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.beaming_down = Player_beam_down(char_type, x, y, scale, speed)
        self.beaming_up = Player_beam_up(char_type, x, y, scale, speed)
        self.beaming = False
        self.space_pressed = False  # Track if spacebar is pressed
        self.start_time = 0  # Track time when spacebar was pressed

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not self.beaming:
                self.beaming = True
                self.space_pressed = True
                self.beaming_down.frame_index = 0
                self.beaming_down.update_time = pygame.time.get_ticks()
                self.start_time = pygame.time.get_ticks()  # Record start time

        elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            if self.space_pressed:
                self.space_pressed = False

    def update(self):
        if self.beaming:
            if not self.space_pressed:  # If spacebar is released
                if not self.beaming_up.frame_index == 0:
                    self.beaming_up.update()
                    if self.beaming_up.frame_index == 0 and pygame.time.get_ticks() - self.beaming_up.update_time > 100:
                        self.beaming = False  # Stop beaming up
                else:
                    self.beaming = False  # Stop beaming up
            else:
                self.beaming_down.update()  # Beam down animation

    def draw(self, screen):
        if self.beaming:
            if not self.space_pressed:  # If spacebar is released
                self.beaming_up.draw(screen)  # Draw beam up
            else:
                self.beaming_down.draw(screen)  # Draw beam down

def main():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('MuFO Targets')

    clock = pygame.time.Clock()
    FPS = 6

    player_scale = 2.5
    player_moving = Player_moving('player', 100, 300, player_scale, 5)
    player_idle1 = Player_idle('player', 600, 300, player_scale, 5)
    player_idle2 = Player_idle('player', 100, 500, player_scale, 5)
    player_idle3 = Player_idle('player', 400, 300, player_scale, 5)
    player_beam = Player_beam('player', 400, 300, player_scale, 5)
    player_beam_up = Player_beam_up('player', 600, 300, player_scale, 5)
    player_beam_down = Player_beam_down('player', 100, 500, player_scale, 5)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            player_beam.handle_input(event)

        screen.fill((0, 128, 0))  # Fill the screen with white

        player_beam.update()
        player_beam.draw(screen)

        player_beam_up.update()
        player_beam_up.draw(screen)

        player_beam_down.update()
        player_beam_down.draw(screen)

        player_moving.update()
        player_moving.draw(screen)

        player_idle1.update()
        player_idle1.draw(screen)

        player_idle2.update()
        player_idle2.draw(screen)

        player_idle3.update()
        player_idle3.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()