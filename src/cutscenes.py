import pygame as pg
import random

pg.font.init()
pg.mixer.init()

# Set resolution
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load game font
font_path = "assets/fonts/press-start-2p.ttf"
font_size = 24
custom_font = pg.font.Font(font_path, font_size)

# Load dialogue sounds
dialogue_sounds = [
    pg.mixer.Sound("assets/sounds/effects/dialogue_1.mp3"),
    pg.mixer.Sound("assets/sounds/effects/dialogue_2.mp3"),
    pg.mixer.Sound("assets/sounds/effects/dialogue_3.mp3"),
    pg.mixer.Sound("assets/sounds/effects/dialogue_4.mp3")
]

# Set dialogue sounds to a quieter volume
for sound in dialogue_sounds:
    sound.set_volume(0.3)

# Load cow image
cow_image = pg.image.load("assets/img/target/moving/people/cow_1/3.png")
cow_image = pg.transform.scale(cow_image, (cow_image.get_width() * 6, cow_image.get_height() * 6))  # Scale the image

# Load moo sound
moo_sound = pg.mixer.Sound("assets/sounds/effects/moo_2.mp3")
moo_sound.set_volume(1.0)  # Set volume to maximum

# Load space ambience sound
space_ambience_sound = pg.mixer.Sound("assets/sounds/effects/space_ambience.mp3")
space_ambience_sound.set_volume(0.5)  # Adjust volume as needed

def draw_text(screen, text, size, color, x, y, center=False):
    font = pg.font.Font(font_path, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

class CutSceneOne:
    
    def __init__(self):

        # Variables
        self.name = 'test'
        self.step = 0
        self.timer = pg.time.get_ticks()
        self.cut_scene_running = True

        # Dialogue
        self.text = {
            'one': "Come in! This is your commander speaking!",
            'two': "We need to prepare for the mission!",
            'three': "We've discovered another planet called ~Earth~.",
            'four': "This planet is filled with different life forms....",
            'five': " ....but one rules them all....",
            'six': "I present to you... COW",
            'seven': "Your mission: capture the COW and bring them in for study.",
            'eight': "Careful, these are highly intelligent beings...",
            'nine': "Make sure to defend yourself if the occasion arises....",
            'ten': "Adventure awaits!!!"
        }
        self.text_counter = 0
        self.space_pressed = False
        self.playing_sound = False  # Track if the sound is currently playing
        self.current_sound = None  # Track the current sound being played

        # Image fade-in properties
        self.cow_opacity = 0
        self.cow_fade_in = False
        self.moo_played = False  # Track if the moo sound has been played

    def update(self):

        pressed = pg.key.get_pressed()
        space = pressed[pg.K_SPACE]

        # Ensure the space bar is pressed and released to move to the next step
        if not space:
            self.space_pressed = True

        current_text = ''
        if self.step == 0:
            current_text = self.text['one']
        elif self.step == 1:
            current_text = self.text['two']
        elif self.step == 2:
            current_text = self.text['three']
        elif self.step == 3:
            current_text = self.text['four']
        elif self.step == 4:
            current_text = self.text['five']
        elif self.step == 5:
            current_text = self.text['six']
        elif self.step == 6:
            current_text = self.text['seven']
        elif self.step == 7:
            current_text = self.text['eight']
        elif self.step == 8:
            current_text = self.text['nine']
        elif self.step == 9:
            current_text = self.text['ten']

        if int(self.text_counter) < len(current_text):
            if not self.playing_sound:
                self.current_sound = random.choice(dialogue_sounds)
                self.current_sound.play(loops=-1)
                self.playing_sound = True
            self.text_counter += 0.4
        else:
            if self.playing_sound:
                self.current_sound.stop()
                self.playing_sound = False
            if space and self.space_pressed:
                self.step += 1
                self.text_counter = 0
                self.space_pressed = False
        if self.step == 6:
            self.cow_fade_in = True

        # Handle cow image fade-in
        if self.cow_fade_in:
            if self.cow_opacity < 255:
                self.cow_opacity += 5
                if not self.moo_played:
                    moo_sound.play()
                    self.moo_played = True
            else:
                self.cow_fade_in = False

        if self.step > 9:
            self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):
        
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                24,
                (255, 255, 255),
                SCREEN_WIDTH // 2,  # Center X
                (SCREEN_HEIGHT // 2) + 200,  # Center Y
                center=True
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                24,
                (255, 255, 255),
                SCREEN_WIDTH // 2,  # Center X
                (SCREEN_HEIGHT // 2) + 200,  # Center Y
                center=True
            )

        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                24,
                (255, 255, 255),
                SCREEN_WIDTH // 2,  # Center X
                (SCREEN_HEIGHT // 2) + 200,  # Center Y
                center=True
            )

        if self.step == 3:
            draw_text(
                screen,
                self.text['four'][0:int(self.text_counter)],
                24,
                (255, 255, 255),
                SCREEN_WIDTH // 2,  # Center X
                (SCREEN_HEIGHT // 2) + 200,  # Center Y
                center=True
            )
            
        if self.step == 4:
            draw_text(
                screen,
                self.text['five'][0:int(self.text_counter)],
                24,
                (255, 255, 255),
                SCREEN_WIDTH // 2,  # Center X
                (SCREEN_HEIGHT // 2) + 200,  # Center Y
                center=True
            )
        
        if self.step == 5:
            draw_text(
                screen,
                self.text['six'][0:int(self.text_counter)],
                24,
                (255, 255, 255),
                SCREEN_WIDTH // 2,  # Center X
                (SCREEN_HEIGHT // 2) + 200,  # Center Y
                center=True
            )

        if self.step == 6:
            draw_text(
                screen,
                self.text['seven'][0:int(self.text_counter)],
                24,
                (255, 255, 255),
                SCREEN_WIDTH // 2,  # Center X
                (SCREEN_HEIGHT // 2) + 200,  # Center Y
                center=True
            )
        
        if self.step == 7:
            draw_text(
                screen,
                self.text['eight'][0:int(self.text_counter)],
                24,
                (255, 255, 255),
                SCREEN_WIDTH // 2,  # Center X
                (SCREEN_HEIGHT // 2) + 200,  # Center Y
                center=True
            )
        
        if self.step == 8:
            draw_text(
                screen,
                self.text['nine'][0:int(self.text_counter)],
                24,
                (255, 255, 255),
                SCREEN_WIDTH // 2,  # Center X
                (SCREEN_HEIGHT // 2) + 200,  # Center Y
                center=True
            )

        if self.step == 9:
            draw_text(
                screen,
                self.text['ten'][0:int(self.text_counter)],
                24,
                (255, 255, 255),
                SCREEN_WIDTH // 2,  # Center X
                (SCREEN_HEIGHT // 2) + 200,  # Center Y
                center=True
            )

        # Draw cow image with fade-in effect
        if self.step >= 6 and self.cow_opacity > 0:
            cow_image.set_alpha(self.cow_opacity)
            cow_rect = cow_image.get_rect(center=(SCREEN_WIDTH // 2 + 400, SCREEN_HEIGHT // 2))
            screen.blit(cow_image, cow_rect)

class CutSceneManager:

    def __init__(self, screen):
        self.cut_scenes_complete = []
        self.cut_scene = None
        self.cut_scene_running = False

        # Drawing variables
        self.screen = screen
        self.window_size = 0

    def start_cut_scene(self, cut_scene):
        if cut_scene.name not in self.cut_scenes_complete:
            self.cut_scenes_complete.append(cut_scene.name)
            self.cut_scene = cut_scene
            self.cut_scene_running = True
            # Play space ambience sound
            space_ambience_sound.play(loops=-1)

    def end_cut_scene(self):
        self.cut_scene = None
        self.cut_scene_running = False
        # Stop space ambience sound
        space_ambience_sound.stop()

    def update(self):
        if self.cut_scene_running:
            self.cut_scene_running = self.cut_scene.update()
        else:
            self.end_cut_scene()

    def draw(self):
        if self.cut_scene_running:
            # Draw specific cut scene details without the black rect
            self.cut_scene.draw(self.screen)