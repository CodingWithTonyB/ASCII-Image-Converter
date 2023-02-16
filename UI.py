import pygame
import os
import tkinter as tk
from tkinter import filedialog
from ASCII import runASCII
from data import output_path
import time

pygame.init()

# Set up the window
win_width = 500
win_height = 700

rect_start_x = 15
rect_start_y = 40

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Image to ASCII converter")

#Image Variables
loaded = False

# Set up font and text for the drop zone
font = pygame.font.Font(None, 30)
text = font.render("Drop a photo here", True, (255, 255, 255))

# Set up the allowed file extensions
allowed_extensions = [".jpg", ".png"]

def handleError():
    pygame.time.set_timer(pygame.USEREVENT, 3000) # Set timer for 3 seconds
    error_text = font.render("Invalid file type", True, (255, 0, 0))
    error_rect = error_text.get_rect(center=drop_zone_rect.center)
    window.blit(error_text, error_rect)
    pygame.display.update()

# Define a function to handle dropping files
def handle_drop_file(file_path):
    # Check if the dropped file has an allowed extension
    if os.path.splitext(file_path)[1] in allowed_extensions:
        print("File dropped:", file_path)
        runASCII(file_path)
    else:
        handleError()

# Set up the drop zone rectangle
drop_zone_rect = pygame.Rect(rect_start_x, rect_start_y, 
                             win_width-(rect_start_x*2), 
                             win_height-(rect_start_y*2))
drop_zone_color = (130, 130, 130)
drop_zone_highlight_color = (150, 150, 150)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Handle file drops
        if event.type == pygame.DROPFILE:
            handle_drop_file(event.file)

        # Handle mouse button down events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if drop_zone_rect.collidepoint(event.pos):
                    # Show the file dialog to allow the user to select a file
                    root = tk.Tk()
                    root.withdraw()
                    file_path = filedialog.askopenfilename()
                    root.destroy()
                    if file_path:
                        handle_drop_file(file_path)
                        
        # Handle mouse hover events
        if event.type == pygame.MOUSEMOTION:
            if drop_zone_rect.collidepoint(event.pos):
                drop_zone_color = drop_zone_highlight_color
            else:
                drop_zone_color = (130, 130, 130)



        # Handle user events
        if event.type == pygame.USEREVENT:
            window.fill((0, 0, 0))

    # Clear the screen
    window.fill((100, 100, 100))

    # Draw the drop zone rectangle
    pygame.draw.rect(window, drop_zone_color, drop_zone_rect)
    pygame.draw.rect(window, (200, 200, 200), drop_zone_rect, 2)

    # Draw the text in the drop zone
    text_rect = text.get_rect(center=drop_zone_rect.center)
    window.blit(text, text_rect)

    # Update the display
    pygame.display.update()
