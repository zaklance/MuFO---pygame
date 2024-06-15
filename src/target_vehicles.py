import pygame
import os

class Target_vehicles(pygame.sprite.Sprite):

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
        folder_path = f'assets/img/target/moving/cars/{class_name}/'
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

class Marquis(Target_vehicles):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Marquis_1_front(Marquis):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Marquis_1_rear(Marquis):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Marquis_1(Marquis):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Marquis_2_front(Marquis):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Marquis_2_rear(Marquis):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Marquis_2(Marquis):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Marquis_3_front(Marquis):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Marquis_3_rear(Marquis):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Marquis_3(Marquis):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Wagon(Target_vehicles):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Wagon_1_front(Wagon):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Wagon_1_rear(Wagon):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Wagon_1(Wagon):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Wagon_2_front(Wagon):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Wagon_2_rear(Wagon):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Wagon_2(Wagon):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Wagon_3_front(Wagon):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Wagon_3_rear(Wagon):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Wagon_3(Wagon):
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
    # marquis_1 = Marquis_1(100, 100, car_scale, 5)
    # marquis_1_front = Marquis_1_front(100, 300, car_scale, 5)
    # marquis_1_rear = Marquis_1_rear(100, 500, car_scale, 5)
    # marquis_2 = Marquis_2(300, 100, car_scale, 5)
    # marquis_2_front = Marquis_2_front(300, 300, car_scale, 5)
    # marquis_2_rear = Marquis_2_rear(300, 500, car_scale, 5)
    # marquis_3 = Marquis_3(700, 100, car_scale, 5)
    # marquis_3_front = Marquis_3_front(700, 300, car_scale, 5)
    # marquis_3_rear = Marquis_3_rear(700, 500, car_scale, 5)

    wagon_1 = Wagon_1(100, 100, car_scale, 5)
    wagon_1_front = Wagon_1_front(100, 300, car_scale, 5)
    wagon_1_rear = Wagon_1_rear(100, 500, car_scale, 5)
    wagon_2 = Wagon_2(300, 100, car_scale, 5)
    wagon_2_front = Wagon_2_front(300, 300, car_scale, 5)
    wagon_2_rear = Wagon_2_rear(300, 500, car_scale, 5)
    wagon_3 = Wagon_3(700, 100, car_scale, 5)
    wagon_3_front = Wagon_3_front(700, 300, car_scale, 5)
    wagon_3_rear = Wagon_3_rear(700, 500, car_scale, 5)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 128, 0))  # Fill the screen with white
        # marquis_1.update()
        # marquis_1.draw(screen)
        # marquis_1_front.update()
        # marquis_1_front.draw(screen)
        # marquis_1_rear.update()
        # marquis_1_rear.draw(screen)
        # marquis_2.update()
        # marquis_2.draw(screen)
        # marquis_2_front.update()
        # marquis_2_front.draw(screen)
        # marquis_2_rear.update()
        # marquis_2_rear.draw(screen)
        # marquis_3.update()
        # marquis_3.draw(screen)
        # marquis_3_front.update()
        # marquis_3_front.draw(screen)
        # marquis_3_rear.update()
        # marquis_3_rear.draw(screen)

        wagon_1.update()
        wagon_1.draw(screen)
        wagon_1_front.update()
        wagon_1_front.draw(screen)
        wagon_1_rear.update()
        wagon_1_rear.draw(screen)
        wagon_2.update()
        wagon_2.draw(screen)
        wagon_2_front.update()
        wagon_2_front.draw(screen)
        wagon_2_rear.update()
        wagon_2_rear.draw(screen)
        wagon_3.update()
        wagon_3.draw(screen)
        wagon_3_front.update()
        wagon_3_front.draw(screen)
        wagon_3_rear.update()
        wagon_3_rear.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()