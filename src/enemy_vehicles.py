import pygame
import os

class Enemy_vehicles(pygame.sprite.Sprite):

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

       # Load images for target
        temp_list = []
        # Count number of files in the folder
        folder_path = f'assets/img/enemy/moving/vehicles/{class_name}/'
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
        if pygame.time.get_ticks() - self.update_time > 100:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]

    def draw(self, screen):
        # Draw the target on the screen
        screen.blit(self.image, self.rect)

class Cop_car(Enemy_vehicles):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Cop_car_1_front(Cop_car):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Cop_car_1_rear(Cop_car):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Cop_car_1(Cop_car):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Abrams(Enemy_vehicles):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class M1_abrams_front(Abrams):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class M1_abrams_rear(Abrams):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class M1_abrams(Abrams):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

def main():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('MuFO Targets')

    clock = pygame.time.Clock()
    FPS = 8

    car_scale = 2
    cop_car_1 = Cop_car_1(200, 100, car_scale, 5)
    cop_car_1_front = Cop_car_1_front(200, 300, car_scale, 5)
    cop_car_1_rear = Cop_car_1_rear(200, 500, car_scale, 5)
    m1_abrams = M1_abrams(500, 100, car_scale, 5)
    m1_abrams_front = M1_abrams_front(500, 300, car_scale, 5)
    m1_abrams_rear = M1_abrams_rear(500, 500, car_scale, 5)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 128, 0))  # Fill the screen with white

        cop_car_1.update()
        cop_car_1.draw(screen)
        cop_car_1_front.update()
        cop_car_1_front.draw(screen)
        cop_car_1_rear.update()
        cop_car_1_rear.draw(screen)
        m1_abrams.update()
        m1_abrams.draw(screen)
        m1_abrams_front.update()
        m1_abrams_front.draw(screen)
        m1_abrams_rear.update()
        m1_abrams_rear.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()