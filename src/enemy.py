import pygame
import os

class Enemies(pygame.sprite.Sprite):

    def __init__(self, x, y, scale, speed=0):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        class_name = self.__class__.__name__.lower()
        
        # Update with more classifications if file names differ even more
        if "bang" in class_name or "snap" in class_name:
            folder_path = f'assets/img/enemy/action/people/{class_name}/'
        else:
            folder_path = f'assets/img/enemy/moving/people/{class_name}/'

        if not os.path.exists(folder_path):
            print(f"Error: Folder '{folder_path}' not found.")
            return  # Or handle the error as appropriate

        temp_list = []
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
        if pygame.time.get_ticks() - self.update_time > 100:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]

    def draw(self, screen):
        # Draw the target on the screen
        screen.blit(self.image, self.rect)

class Cop_1(Enemies):
    def __init__(self, x, y, scale, speed=0):
        super().__init__(x, y, scale, speed)

class Cop_1_Bang(Enemies):
    def __init__(self, x, y, scale, speed=0):
        super().__init__(x, y, scale, speed)

class Cop_2(Enemies):
    def __init__(self, x, y, scale, speed=0):
        super().__init__(x, y, scale, speed)

class Cop_2_Bang(Enemies):
    def __init__(self, x, y, scale, speed=0):
        super().__init__(x, y, scale, speed)

class Conspiracy(Enemies):
    def __init__(self, x, y, scale, speed=0):
        super().__init__(x, y, scale, speed)

class Conspiracy_Snap(Enemies):
    def __init__(self, x, y, scale, speed=0):
        super().__init__(x, y, scale, speed)


def main():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('MuFO Targets')

    clock = pygame.time.Clock()
    FPS = 4

    cop_scale = 2.5
    cop_1 = Cop_1(100, 100, cop_scale, 5)
    cop_2 = Cop_2(300, 300, cop_scale, 5)
    cop_1_bang = Cop_1_Bang(100, 300, cop_scale, 5)
    cop_2_bang = Cop_2_Bang(300, 500, cop_scale, 5)
    conspiracy = Conspiracy(500, 300, cop_scale, 5)
    conspiracy_snap = Conspiracy_Snap(500, 500, cop_scale, 5)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 128, 0))
        cop_1.update()
        cop_1.draw(screen) 

        cop_2.update()
        cop_2.draw(screen) 

        conspiracy.update()
        conspiracy.draw(screen)

        cop_1_bang.update()
        cop_1_bang.draw(screen) 

        cop_2_bang.update()
        cop_2_bang.draw(screen)

        conspiracy_snap.update()
        conspiracy_snap.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()