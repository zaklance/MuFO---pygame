from PIL import Image, ImageSequence
import os

gif_path = "assets/gif/stars.gif"
output_folder = "assets/frames"

# Extract frames from the GIF
with Image.open(gif_path) as im:
    for i, frame in enumerate(ImageSequence.Iterator(im)):
        frame = frame.convert('RGB')
        frame = frame.resize((1600, 900))
        frame.save(f"{output_folder}/frame_{i}.png")