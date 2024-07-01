import pygame
import os
import random
from pygame.math import Vector2
from pygame.sprite import AbstractGroup
from player import Character
from settings import SCROLL_THRESH, SCREEN_WIDTH, SCREEN_HEIGHT, screen, screen_scroll, bg_scroll

# Target Classes: 
# Cows: Cow_1, Cow_2, Cow_3
# Chickens: Chicken_1, Chicken_2
# Civilians: Man_1, Man_2, Woman_1, Woman_2


class Targets(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed=0):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.speed = speed
        self.direction = 1
        self.direction_y = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        # ai variables
        self.move_counter = 0

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

        self.image_orig = self.animation_list[0][-1]
        self.image = self.image_orig.copy()  
        
        self.rect = self.image.get_rect(topleft=(x, y))
        self.rect.center = (x, y)

    def ai(self):
        if self.alive and Character.alive:
            rand_num = random.randint(6, 24)
            rand_dir = random.choice([1, 2, 3, 4])                
            ai_moving_right = False
            ai_moving_left = False
            ai_moving_up = False
            ai_moving_down = False
            if self.direction == 1:
                ai_moving_right = True
            elif self.direction == -1:
                ai_moving_right = False
            if self.direction_y == 1:
                ai_moving_up = True
            elif self.direction_y == -1:
                ai_moving_down = True
            ai_moving_left = not ai_moving_right
            ai_moving_down = not ai_moving_up
            self.move(ai_moving_right,ai_moving_left, ai_moving_up, ai_moving_down)
            self.move_counter += 1

            if self.move_counter > rand_num:
                if rand_dir == 1:
                    self.direction = 1
                    self.move_counter *= -1
                if rand_dir == 2: # 2 when with up down direction
                    self.direction = -1
                    self.move_counter *= -1
                if rand_dir == 3:
                    self.direction_y = 1
                    self.move_counter *= -1
                if rand_dir == 4:
                    self.direction_y = -1
                    self.move_counter *= -1

    def move(self, moving_right, moving_left, moving_up, moving_down): # , moving_up, moving_down
        screen_scroll = Vector2(0, 0)
        dx = 0
        dy = 0
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
            screen_scroll[0] = dx
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
            screen_scroll[0] = dx
        if moving_up:
            dy = -self.speed
            screen_scroll[1] = dy
        if moving_down:
            dy = self.speed
            screen_scroll[1] = dy
            
        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy

        return screen_scroll
   
    def update(self):
        # Update animation frames
        if pygame.time.get_ticks() - self.update_time > 100:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]

    def draw(self, screen, bg_scroll):
        # Draw the target on the screen
        screen.blit(pygame.transform.flip(self.image, self.flip, False), ((self.rect.x + bg_scroll[0]), (self.rect.y + bg_scroll[1])))


class Target_Object(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        super().__init__()
        self.image = pygame.transform.scale(self.image_orig, (int(self.image_orig.get_width() * scale), int(self.image_orig.get_height() * scale)))
        self.rect = self.image.get_rect(center=(x,y))

class Cows(Targets):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Basic_Cow(Cows):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Best_Cow(Cows):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Cow_1(Basic_Cow):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

class Cow_2(Basic_Cow):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)

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