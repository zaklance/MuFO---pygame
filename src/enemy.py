import pygame
import os

class Cop_1(pygame.sprite.Sprite):

    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        class_name = self.__class__.__name__.lower()        

        # Load images for target
        temp_list = []
        # Count number of files in the folder
        folder_path = f'assets/img/enemy/moving/people/{class_name}/'
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

def main():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('MuFO Targets')

    clock = pygame.time.Clock()
    FPS = 8

    cop_scale = 2.5
    cop_1 = Cop_1('cop_1', 700, 100, cop_scale, 5)
    # cop_2 = Man_2('cop_2', 300, 700, cop_scale, 5)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 128, 0))
        cop_1.update()
        cop_1.draw(screen) 

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()