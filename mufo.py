import pygame
import os

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Mû.F.O')

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define player action variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

#define colors
BG = (144, 201, 120)

# Load background frames
background_frames = []
frame_folder = "assets/frames"
for filename in sorted(os.listdir(frame_folder)):
    if filename.endswith(".png"):
        frame = pygame.image.load(os.path.join(frame_folder, filename))
        background_frames.append(frame)

print(f"Loaded {len(background_frames)} frames.")

current_frame = 0

# Sound effects
selector_sound = pygame.mixer.Sound("assets/sounds/effects/selector.mp3")
selected_sound = pygame.mixer.Sound("assets/sounds/effects/selected.mp3")

def draw_bg():
    global current_frame
    screen.blit(background_frames[current_frame], (0, 0))
    current_frame = (current_frame + 1) % len(background_frames)

class Button():
    def __init__(self, text, x, y, width, height, color, selected_color, function):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.selected_color = selected_color
        self.function = function
        self.font = pygame.font.Font(None, 40)
        self.selected = False

    def draw(self, screen):
        color = self.selected_color if self.selected else self.color
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))

        text_surf = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=((self.x + self.width // 2), (self.y + self.height // 2)))
        screen.blit(text_surf, text_rect)

    def click(self):
        self.function()

def start_game():
    global game_active
    game_active = True
    # pygame.mixer.music.stop()

def show_leaderboard():
    # show leaderboard page
    pass

def quit_game():
    pygame.quit()
    exit()

def title_screen():
    pygame.mixer.music.load("assets/sounds/music/title_screen.mp3")
    pygame.mixer.music.play(-1)

    buttons = [
        Button('Start', SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 100, 200, 50, (0, 200, 0), (0, 255, 0), start_game),
        Button('Leaderboard', SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50, (0, 0, 200), (0, 0, 255), show_leaderboard),
        Button('Quit', SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100, 200, 50, (200, 0, 0), (255, 0, 0), quit_game)
    ]

    selected_button = 0
    buttons[selected_button].selected = True

    while not game_active:
        draw_bg()

        for button in buttons:
            button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    buttons[selected_button].selected = False
                    selected_button = (selected_button - 1) % len(buttons)
                    buttons[selected_button].selected = True
                    selector_sound.play()
                if event.key == pygame.K_DOWN:
                    buttons[selected_button].selected = False
                    selected_button = (selected_button + 1) % len(buttons)
                    buttons[selected_button].selected = True
                    selector_sound.play()
                if event.key == pygame.K_SPACE:
                    buttons[selected_button].click()
                    selected_sound.play()
        
        pygame.display.update()
        clock.tick(FPS)

class Character(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        img_path = f'assets/img/{self.char_type}/idle/0.png'
        img = pygame.image.load(img_path)
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, moving_left, moving_right, moving_up, moving_down):
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

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

player = Character('player', 200, 200, 2, 5)  
target = Character('target', 800, 450, .15, 5)  

game_active = False

def main():
    global game_active
    
    while True:
        if not game_active:
            title_screen()
        else:
            run_game()

def run_game():
    global game_active, moving_left, moving_right, moving_up, moving_down

    run = True
    while run:
        clock.tick(FPS)
        draw_bg()

        player.draw()
        target.draw()

        player.move(moving_left, moving_right, moving_up, moving_down)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moving_left = True
                if event.key == pygame.K_d:
                    moving_right = True
                if event.key == pygame.K_w:
                    moving_up = True
                if event.key == pygame.K_s:
                    moving_down = True
                if event.key == pygame.K_ESCAPE:
                    game_active = False
                    run = False
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_d:
                    moving_right = False
                if event.key == pygame.K_w:
                    moving_up = False
                if event.key == pygame.K_s:
                    moving_down = False

        pygame.display.update()

    pygame.quit()
    exit()

main()