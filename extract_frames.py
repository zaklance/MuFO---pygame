from PIL import Image, ImageSequence
import os

# Paths
gif_path = "assets/gif/stars.gif"  # Path to the GIF file
output_folder = "assets/frames"  # Folder to save the extracted frames

# Extract frames from the GIF
with Image.open(gif_path) as im:
    for i, frame in enumerate(ImageSequence.Iterator(im)):
        frame = frame.convert('RGB')
        frame = frame.resize((1600, 900))  # Resize to 1600x900
        frame.save(f"{output_folder}/frame_{i}.png")