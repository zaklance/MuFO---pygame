from mouse import MouseControl
import pygame
import os
from map import load_game_bg, draw_game_bg, update_bg_scroll, Building
from leaderboard import Result, Game, Score
from target import Targets
from enemy import Enemies

# Load pygame
pygame.init()

# Load mixer mode for music
pygame.mixer.init()

# Load database initializer
Game.initialize_database()

# Set resolution
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set Window Name
pygame.display.set_caption('Mû.F.O')

# Set framerate
clock = pygame.time.Clock()
FPS = 60

# Global screen state
current_screen = "title"

# Define player action variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

# Define scrolling variables
scroll_thresh = SCREEN_WIDTH // 2
screen_scroll = [0, 0]
bg_scroll = [0, 0]

# Load sound effects
script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, "assets", "sounds", "effects")

navigation_sound_path = os.path.join(assets_dir, "navigation.mp3")
selected_sound_path = os.path.join(assets_dir, "selected.mp3")

navigation_sound = pygame.mixer.Sound(navigation_sound_path)
selected_sound = pygame.mixer.Sound(selected_sound_path)

# Global game state
game_active = False
paused = False

# Define global variable for Score
current_score = Score(None, None)

# Targets and Enemies Sprite groups 
targets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Load background frames for title screen
current_frame = 0
background_frames = []
frame_folder = "assets/frames"
for filename in sorted(os.listdir(frame_folder)):
    if filename.endswith(".png"):
        frame = pygame.image.load(os.path.join(frame_folder, filename))
        background_frames.append(frame)
print(f"Loaded {len(background_frames)} frames.")

# Load game font
font_path = "assets/fonts/press-start-2p.ttf"
font_size = 24
custom_font = pygame.font.Font(font_path, font_size)

# Create Button
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
        self.font = pygame.font.Font(font_path, 20)
        self.selected = False

    def draw(self, screen):
        color = self.selected_color if self.selected else self.color
        text_surf = self.font.render(self.text, True, color)
        text_rect = text_surf.get_rect(center=(self.x, self.y))
        screen.blit(text_surf, text_rect)

    def click(self):
        selected_sound.play()
        self.function()

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        super().__init__()
        self.animation_list = []
        self.flip = False
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.speed = speed
        self.load_images('idle', scale)
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def load_images(self, action, scale):
        self.animation_list = []
        folder_path = f'assets/img/player/{action}/'
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
            self.animation_list.append(img)

class Player_idle(Character):
    def __init__(self, x, y, scale, speed):
        super().__init__(x, y, scale, speed)
        self.load_images('idle', scale)
        self.image = self.animation_list[0]

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
        self.opacity = 255

    def set_opacity(self, opacity):
        self.opacity = opacity
        for img in self.animation_list: 
            img.set_alpha(self.opacity)

    def start_beam(self):
        self.is_beam_active = True
        self.reverse = False

    def end_beam(self):
        self.reverse = True

    def update(self, player_rect):
        if self.is_beam_active:
            self.rect.center = player_rect.center
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
        if self.is_beam_active:
            screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

# player_beam_down = Player_beam_down(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 2, 5)
# player = Player_idle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 2, 5)

# player_beam_down.set_opacity(128)

# Define the threshold area
threshold_x = SCREEN_WIDTH // 3
threshold_y = SCREEN_HEIGHT // 4

# Initialize MouseControl
mouse_control = MouseControl()

def draw_title_bg(background_frames):
    global current_frame
    screen.blit(background_frames[current_frame], (0, 0))
    current_frame = (current_frame + 1) % len(background_frames)

def start_game():
    global game_active, paused, current_screen
    game_active = True
    paused = False
    current_screen = "game"
    
    pygame.mixer.music.load("assets/sounds/music/in_game.mp3")
    pygame.mixer.music.play(-1)

def show_leaderboard():
    global game_active
    game_active = True
    leaderboard_data = Result.get_leaderboard()
    print(f"Leaderboard data to display: {leaderboard_data}")

    colors = [
        (192, 192, 192), (192, 192, 192),  # Silver
        (255, 165, 0), (255, 165, 0),      # Orange
        (0, 0, 255), (0, 0, 255),          # Blue
        (0, 128, 0), (0, 128, 0),          # Green
        (255, 0, 0), (255, 0, 0)           # Red
    ]

    trophy_image = pygame.image.load('assets/img/leaderboard/trophy.png')
    trophy_image = pygame.transform.scale(trophy_image, (40, 40))

    while game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_active = False  # Exit leaderboard screen on ESC key

        draw_title_bg(background_frames)  # Use the same background animation as the title screen
        
        title = custom_font.render("LEADERBOARD", True, (255, 255, 0))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 50))

        trophy_width, trophy_height = trophy_image.get_size()
        screen.blit(trophy_image, (SCREEN_WIDTH // 2 - title.get_width() // 2 - trophy_width - 10, 50))  # Left side
        screen.blit(trophy_image, (SCREEN_WIDTH // 2 + title.get_width() // 2 + 10, 50))  # Right side

        # Determine maximum width needed for the name column
        max_name_width = max(custom_font.size(username)[0] for username, game_title, score in leaderboard_data[:10])
        score_width = max(custom_font.size(f'{score}')[0] for _, _, score in leaderboard_data[:10])

        # Display column headers with increased spacing
        name_header = custom_font.render("Name", True, (255, 255, 255))
        score_header = custom_font.render("Score", True, (255, 255, 255))
        header_x = SCREEN_WIDTH // 2 - (name_header.get_width() + score_header.get_width()) // 2
        screen.blit(name_header, (header_x, 150))
        screen.blit(score_header, (header_x + max_name_width + 150, 150))  # Adjusting spacing

        y_offset = 200
        rank_x = SCREEN_WIDTH // 2 - 300

        # Display placeholders for ranks in the first column
        for i in range(10):
            rank_text = custom_font.render(f"{i + 1}", True, colors[i])
            screen.blit(rank_text, (rank_x, y_offset + i * 40))

        # Display actual leaderboard data with increased spacing
        for i, (username, game_title, score) in enumerate(leaderboard_data[:10]):
            username_text = custom_font.render(f"{username}", True, colors[i])
            username_x = header_x + (max_name_width - username_text.get_width()) // 2
            screen.blit(username_text, (header_x, y_offset + i * 40))

            score_text = custom_font.render(f"{score}", True, colors[i])
            screen.blit(score_text, (header_x + max_name_width + 150, y_offset + i * 40))  # Adjusting spacing

        pygame.display.update()
        clock.tick(FPS)

def pause_screen():
    global paused, current_frame

    buttons = [
        Button('Resume', SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100, 200, 50, (100, 100, 100), (255, 255, 255), resume_game),
        Button('Leaderboard', SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 200, 50, (100, 100, 100), (255, 255, 255), show_leaderboard),
        Button('Back to Menu', SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100, 200, 50, (100, 100, 100), (255, 255, 255), title_screen),
        Button('Quit', SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200, 200, 50, (100, 100, 100), (255, 255, 255), quit_game)
    ]

    selected_button = 0
    buttons[selected_button].selected = True

    while paused:
        draw_title_bg(background_frames)  # Use the same background animation as the title screen

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
                    navigation_sound.play()
                if event.key == pygame.K_DOWN:
                    buttons[selected_button].selected = False
                    selected_button = (selected_button + 1) % len(buttons)
                    buttons[selected_button].selected = True
                    navigation_sound.play()
                if event.key == pygame.K_SPACE:
                    buttons[selected_button].click()
        
        pygame.display.update()
        clock.tick(FPS)

def quit_game():
    pygame.quit()
    exit()

def resume_game():
    global paused, game_active
    paused = False
    game_active = True

def title_screen():
    global current_screen
    current_screen = "title"
    
    pygame.mixer.music.load("assets/sounds/music/title_screen.mp3")
    pygame.mixer.music.play(-1)

    buttons = [
        Button('Start', SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100, 200, 50, (100, 100, 100), (255, 255, 255), start_game),
        Button('Leaderboard', SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 200, 50, (100, 100, 100), (255, 255, 255), show_leaderboard),
        Button('Quit', SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100, 200, 50, (100, 100, 100), (255, 255, 255), quit_game)
    ]

    selected_button = 0
    buttons[selected_button].selected = True

    earth_image = pygame.image.load("assets/img/general/earth.png")
    earth_image = pygame.transform.scale(earth_image, (int(earth_image.get_width() * 6), int(earth_image.get_height() * 6)))
    earth_rect = earth_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 1060))
    
    angle = 0

    while current_screen == "title":
        draw_title_bg(background_frames)
        
        # Increment the angle for rotation
        angle += .05
        if angle == 360:
            angle = 0

        # Rotate the earth image
        rotated_earth_image = pygame.transform.rotate(earth_image, angle)
        rotated_earth_rect = rotated_earth_image.get_rect(center=earth_rect.center)
        screen.blit(rotated_earth_image, rotated_earth_rect)

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
                    navigation_sound.play()
                if event.key == pygame.K_DOWN:
                    buttons[selected_button].selected = False
                    selected_button = (selected_button + 1) % len(buttons)
                    buttons[selected_button].selected = True
                    navigation_sound.play()
                if event.key == pygame.K_SPACE:
                    buttons[selected_button].click()
                    selected_sound.play()
        
        pygame.display.update()
        clock.tick(FPS)

def run_game():
    global game_active, paused, moving_left, moving_right, moving_up, moving_down, screen_scroll, bg_scroll, current_score
    
    # Load game background image for active play
    game_bg = load_game_bg("assets/img/map/map-0.png")
    bg_width = game_bg.get_width()
    bg_height = game_bg.get_height()
    field = load_game_bg("assets/img/map/map-1.png")

    player_beam_down = Player_beam_down(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 2, 5)
    player = Player_idle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 2, 5)

    # Create buildings
    # Row 1, Block 1
    watertower = Building('watertower', 1051, 1169)
    house_4a_1 = Building('house_4a', 1713, 1368, True)  # This one is not flipped
    house_2a_1 = Building('house_2a', 1903, 1368, True)
    house_1a_1 = Building('house_1a', 2092, 1365) # This one is not flipped
    house_3b_1 = Building('house_3b', 2282, 1370, True)
    # Row 1, Block 2
    house_1c_1 = Building('house_1c', 2813, 1365, True)
    house_4a_2 = Building('house_4a', 3002, 1368, True)
    circus = Building('circus', 3388, 1360)
    # Row 2, Block 1
    house_4b_1 = Building('house_4b', 1145, 1726)
    house_1a_2 = Building('house_1a', 1524, 1724, True)
    house_1c_2 = Building('house_1c', 1713, 1724, True)
    house_3a_1 = Building('house_3a', 1903, 1729, True)
    house_2c_1 = Building('house_2c', 2092, 1725)
    house_1a_3 = Building('house_1a', 2282, 1724)
    # Row 2, Block 2
    house_2a_2 = Building('house_2a', 2623, 1725, True)
    house_1b_1 = Building('house_1b', 2813, 1724)
    house_3b_2 = Building('house_3b', 3002, 1725, True)
    house_4a_3 = Building('house_4a', 3192, 1726, True)
    house_1a_4 = Building('house_1a', 3382, 1724, True)
    house_2c_2 = Building('house_2c', 3761, 1725)
    house_1c_3 = Building('house_1c', 3950, 1724, True)
    # Row 3, Block 1
    house_1b_2 = Building('house_1b', 803, 2093)
    house_3a_2 = Building('house_3a', 1145, 2099)
    house_2b_1 = Building('house_2b', 1334, 2093, True)
    house_1b_3 = Building('house_1b', 1713, 2093)
    house_4b_2 = Building('house_4b', 1903, 2096, True)
    grocery = Building('grocery', 2092, 1994)
    # Row 3, Block 2
    church = Building('church', 2623, 2095)
    house_2b_2 = Building('house_2b', 3002, 2095, True)
    house_3a_3 = Building('house_3a', 3192, 2094, True)
    house_1b_4 = Building('house_1b', 3382, 2093, True)
    house_1a_5 = Building('house_1a', 3571, 2093)
    house_4a_4 = Building('house_4a', 3762, 2096)
    house_2a_2 = Building('house_2a', 3950, 2095)
    # Row 4, Block 1
    house_1c_4 = Building('house_1c', 1524, 2452, True)
    house_3a_4 = Building('house_3a', 1713, 2453)
    house_2a_3 = Building('house_2a', 1903, 2455, True)
    house_4a_5 = Building('house_4a', 2092, 2454, True)
    house_1b_5 = Building('house_1b', 2282, 2452, True)
    # Row 4, Block 2
    house_3b_3 = Building('house_3b', 2623, 2454, True)
    house_1a_6 = Building('house_1a', 2813, 2452)
    house_1b_6 = Building('house_1b', 3002, 2452)
    house_4a_6 = Building('house_4a', 3192, 2454, True)
    house_2c_3 = Building('house_2c', 3382, 2454)
    house_1c_5 = Building('house_1c', 3571, 2452)
    house_1a_7 = Building('house_1a', 3950, 2452, True)
    # Row 5, Block 1
    house_1a_8 = Building('house_1a', 1903, 2821)
    house_3b_4 = Building('house_3b', 2092, 2822, True)
    house_3a_5 = Building('house_3a', 2282, 2827)
    # Row 5, Block 2
    house_1c_6 = Building('house_1c', 2623, 2821, True)
    house_3a_6 = Building('house_3a', 2813, 2827)
    house_2a_4 = Building('house_2a', 3002, 2823)
    house_1b_7 = Building('house_1b', 3192, 2821)
    house_4a_7 = Building('house_4a', 3571, 2824)
    house_2b_3 = Building('house_2b', 3761, 2823, True)
    house_3b_5 = Building('house_3b', 3950, 2827)
    # Row 6, Block 1
    house_1a_9 = Building('house_1a', 1524, 3180, True)
    house_4b_3 = Building('house_4b', 2623, 3183, True)
    house_2b_4 = Building('house_2b', 2813, 3182)
    house_1c_7 = Building('house_1c', 3382, 3180, True)
    school = Building('school', 3972, 3202)
    wheat = Building('wheat', 521, 3966)

    while game_active:
        clock.tick(FPS)

        # Draw the game background
        draw_game_bg(screen, game_bg, bg_scroll)

        # Draw buildings
        # Row 1, Block 1
        watertower.draw(field)
        house_4a_1.draw(field)
        house_2a_1.draw(field)
        house_1a_1.draw(field)
        house_3b_1.draw(field)
        # Row 1, Block 2
        house_1c_1.draw(field)
        house_4a_2.draw(field)
        circus.draw(field)
        # Row 2, Block 1
        house_4b_1.draw(field)
        house_1a_2.draw(field)
        house_1c_2.draw(field)
        house_3a_1.draw(field)
        house_2c_1.draw(field)
        house_1a_3.draw(field)
        # Row 2, Block 2
        house_2a_2.draw(field)
        house_1b_1.draw(field)
        house_3b_2.draw(field)
        house_4a_3.draw(field)
        house_1a_4.draw(field)
        house_2c_2.draw(field)
        house_1c_3.draw(field)
        # Row 3, Block 1
        house_1b_2.draw(field)
        house_3a_2.draw(field)
        house_2b_1.draw(field)
        house_1b_3.draw(field)
        house_4b_2.draw(field)
        grocery.draw(field)
        # Row 3, Block 2
        church.draw(field)
        house_2b_2.draw(field)
        house_3a_3.draw(field)
        house_1b_4.draw(field)
        house_1a_5.draw(field)
        house_4a_4.draw(field)
        house_2a_2.draw(field)
        # Row 4, Block 1
        house_1c_4.draw(field)
        house_3a_4.draw(field)
        house_2a_3.draw(field)
        house_4a_5.draw(field)
        house_1b_5.draw(field)
        # Row 4, Block 2
        house_3b_3.draw(field)
        house_1b_6.draw(field)
        house_1a_6.draw(field)
        house_4a_6.draw(field)
        house_2c_3.draw(field)
        house_1c_5.draw(field)
        house_1a_7.draw(field)
        # Row 5, Block 1
        house_1a_8.draw(field)
        house_3b_4.draw(field)
        house_3a_5.draw(field)
        # Row 5, Block 2
        house_1c_6.draw(field)
        house_3a_6.draw(field)
        house_2a_4.draw(field)
        house_1b_7.draw(field)
        house_4a_7.draw(field)
        house_2b_3.draw(field)
        house_3b_5.draw(field)
        # Row 6, Block 1
        house_1a_9.draw(field)
        house_4b_3.draw(field)
        house_2b_4.draw(field)
        house_1c_7.draw(field)
        school.draw(field)
        wheat.draw(field)

        # Always draw beam first so it appears behind the player
        player_beam_down.update(player.rect)
        player_beam_down.draw()

        player.update()
        player.draw()

        screen_scroll = player.move(moving_left, moving_right, moving_up, moving_down, threshold_x, threshold_y)
        bg_scroll = update_bg_scroll(bg_scroll, screen_scroll, bg_width, bg_height, SCREEN_WIDTH, SCREEN_HEIGHT)

        # Update mouse control
        mouse_control.update(screen)

        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
                current_score.save_score()
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
                    paused = True
                    pause_screen()  
                if event.key == pygame.K_SPACE:
                    player_beam_down.spacebar_held = True
                    if not player_beam_down.is_beam_active:
                        player_beam_down.start_beam()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_d:
                    moving_right = False
                if event.key == pygame.K_w:
                    moving_up = False
                if event.key == pygame.K_s:
                    moving_down = False
                if event.key == pygame.K_SPACE:
                    player_beam_down.spacebar_held = False
                    player_beam_down.end_beam()

            # Process mouse events
            mouse_control.process_events(event)

        pygame.display.update()

    current_score.save_score()
    pygame.quit()
    exit()

def main():
    global game_active
    
    while True:
        if current_screen == "title":
            title_screen()
        elif current_screen == "game":
            run_game()
        elif current_screen == "leaderboard":
            show_leaderboard() 
main()