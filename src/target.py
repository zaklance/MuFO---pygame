import pygame
import os

# Target Classes: 
# Cows: Cow_1, Cow_2, Cow_3
# Chickens: Chicken_1, Chicken_2
# People Man_1, Man_2, Woman_1, Woman_2

class Cow_1(pygame.sprite.Sprite):

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

        #load images for target
        temp_list = []
        #count number of files in the folder
        num_of_frames = len(os.listdir(f'assets/img/target/moving/people/{class_name}/'))
        for i in range(num_of_frames):
            img = pygame.image.load(f'assets/img/target/moving/people/{class_name}/{i}.png')
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

class Cow_2(pygame.sprite.Sprite):

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

        #load images for target
        temp_list = []
        #count number of files in the folder
        num_of_frames = len(os.listdir(f'assets/img/target/moving/people/{class_name}/'))
        for i in range(num_of_frames):
            img = pygame.image.load(f'assets/img/target/moving/people/{class_name}/{i}.png')
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

class Cow_3(pygame.sprite.Sprite):

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

        #load images for target
        temp_list = []
        #count number of files in the folder
        num_of_frames = len(os.listdir(f'assets/img/target/moving/people/{class_name}/'))
        for i in range(num_of_frames):
            img = pygame.image.load(f'assets/img/target/moving/people/{class_name}/{i}.png')
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

class Chicken_1(pygame.sprite.Sprite):

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

        #load images for target
        temp_list = []
        #count number of files in the folder
        num_of_frames = len(os.listdir(f'assets/img/target/moving/people/{class_name}/'))
        for i in range(num_of_frames):
            img = pygame.image.load(f'assets/img/target/moving/people/{class_name}/{i}.png')
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

class Chicken_2(pygame.sprite.Sprite):

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

        #load images for target
        temp_list = []
        #count number of files in the folder
        num_of_frames = len(os.listdir(f'assets/img/target/moving/people/{class_name}/'))
        for i in range(num_of_frames):
            img = pygame.image.load(f'assets/img/target/moving/people/{class_name}/{i}.png')
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

class Man_1(pygame.sprite.Sprite):

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
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > 100:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0

    def draw(self, screen):
        # Draw the target on the screen
        screen.blit(self.image, self.rect)

class Man_2(pygame.sprite.Sprite):

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

        #load images for target
        temp_list = []
        #count number of files in the folder
        num_of_frames = len(os.listdir(f'assets/img/target/moving/people/{class_name}/'))
        for i in range(num_of_frames):
            img = pygame.image.load(f'assets/img/target/moving/people/{class_name}/{i}.png')
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

class Woman_1(pygame.sprite.Sprite):

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
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > 100:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0

    def draw(self, screen):
        # Draw the target on the screen
        screen.blit(self.image, self.rect)

class Woman_2(pygame.sprite.Sprite):

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

    # Create an instance of Cow_1 for testing
    cow_scale = 2.5
    cow_1 = Cow_1('cow_1', 100, 100, cow_scale, 5)
    cow_2 = Cow_2('cow_2', 100, 300, cow_scale, 5)
    cow_3 = Cow_3('cow_3', 100, 500, cow_scale, 5)

    chicken_scale = 2.5
    chicken_1 = Chicken_1('chicken_1', 300, 100, chicken_scale, 5)
    chicken_2 = Chicken_2('chicken_2', 300, 300, chicken_scale, 5)

    man_scale = 2.5
    man_1 = Man_1('man_1', 500, 100, man_scale, 5)
    man_2 = Man_2('man_2', 500, 300, man_scale, 5)

    woman_scale = 2.5
    woman_1 = Woman_1('woman_1', 300, 500, woman_scale, 5)
    woman_2 = Woman_2('woman_2', 500, 500, woman_scale, 5)

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