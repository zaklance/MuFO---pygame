import pygame
import os
import random

# Target Classes: 
# Cows: Cow_1, Cow_2, Cow_3
# Chickens: Chicken_1, Chicken_2
# Civilians: Man_1, Man_2, Woman_1, Woman_2

class Targets(pygame.sprite.Sprite):

    def __init__(self, x, y, scale, speed=0):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        self.dx = 0
        self.dy = 0

        class_name = self.__class__.__name__.lower()        

       # Load images for target
        temp_list = []
        # Count number of files in the folder
        folder_path = f'assets/img/target/moving/people/{class_name}/'
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

<<<<<<< HEAD
=======
        if isinstance(self, Cows):
            self.x += self.dx
            self.y += self.dy

>>>>>>> groups
    def draw(self, screen):
        # Draw the target on the screen
        screen.blit(self.image, self.rect)

class Cows(Targets):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)
        self.dx = 0
        self.dy = 0

class Basic_Cow(Cows):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)
        self.dx = random.randint(-2, 2)
        self.dy = random.randint(-2, 2)
        self.x = x
        self.y = y

class Best_Cow(Cows):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Cow_1(Basic_Cow):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)
        self.dx = random.randint(-2, 2)
        self.dy = random.randint(-2, 2)
        self.x = x
        self.y = y

class Cow_2(Basic_Cow):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)
        self.dx = random.randint(-2, 2)
        self.dy = random.randint(-2, 2)
        self.x = x
        self.y = y

class Cow_3(Best_Cow):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Chickens(Targets):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Chicken_1(Chickens):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Chicken_2(Chickens):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Civilians(Targets):
    def __init__(self, x, y, scale, speed=0):
        super().__init__(x, y, scale, speed)

class Man_1(Civilians):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Man_2(Civilians):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Woman_1(Civilians):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Woman_2(Civilians):
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

    # Create an instance of Cow_1 for testing
    cow_scale = 2.5
    cow_1 = Cow_1(100, 100, cow_scale, 5)
    cow_2 = Cow_2(100, 300, cow_scale, 5)
    cow_3 = Cow_3(100, 500, cow_scale, 5)

    chicken_scale = 2.5
    chicken_1 = Chicken_1(300, 100, chicken_scale, 5)
    chicken_2 = Chicken_2(300, 300, chicken_scale, 5)

    man_scale = 2.5
    man_1 = Man_1(500, 100, man_scale, 5)
    man_2 = Man_2(500, 300, man_scale, 5)

    woman_scale = 2.5
    woman_1 = Woman_1(300, 500, woman_scale, 5)
    woman_2 = Woman_2(500, 500, woman_scale, 5)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 128, 0))  # Fill the screen with white
        cow_1.update()  # Update the cow's animation
        cow_1.draw(screen)  # Draw the cow on the screen
        cow_2.update()
        cow_2.draw(screen)
        cow_3.update()
        cow_3.draw(screen)

        chicken_1.update()
        chicken_1.draw(screen) 
        chicken_2.update() 
        chicken_2.draw(screen)  

        man_1.update()
        man_1.draw(screen) 
        man_2.update() 
        man_2.draw(screen) 

        woman_1.update()
        woman_1.draw(screen) 
        woman_2.update() 
        woman_2.draw(screen)   

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()