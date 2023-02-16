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
rect_start_y = 50

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Image to ASCII converter")

#Image Variables
loaded = False

# Set up font and text
font = pygame.font.Font(None, 30)
font_select = pygame.font.Font(None, 15)
text_drop = font.render("Drop a photo here", True, (255, 255, 255))
text_select = font_select.render("Select File", True, (255, 255, 255))

# Set up the allowed file extensions
allowed_extensions = [".jpg", ".png"]

def handleError():
    print('invalid file type')

# Define a function to handle dropping files
def handle_drop_file(file_path):
    # Check if the dropped file has an allowed extension
    if os.path.splitext(file_path)[1] in allowed_extensions:
        print("File dropped:", file_path)
        runASCII(file_path)
    else:
        handleError()


# Set up the button to select using file
select_using_file_rect = pygame.Rect(15,10,80,30)
select_using_color = (130, 130, 130)
select_using_highlight_color = (150, 150, 150)

# Set up the drop zone rectangle
drop_zone_rect = pygame.Rect(rect_start_x, rect_start_y, 
                             win_width-(rect_start_x*2), 
                             win_height-(rect_start_y+10))
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
                if select_using_file_rect.collidepoint(event.pos):
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
        if event.type == pygame.MOUSEMOTION:
            if select_using_file_rect.collidepoint(event.pos):
                select_using_color = select_using_highlight_color
            else:
                select_using_color = (130, 130, 130)

        # Handle user events
        if event.type == pygame.USEREVENT:
            window.fill((0, 0, 0))

    # Clear the screen
    window.fill((100, 100, 100))
    boundry_color = (200,200,200)
    # Draw the drop zone rectangle
    pygame.draw.rect(window, drop_zone_color, drop_zone_rect)
    pygame.draw.rect(window, boundry_color, drop_zone_rect, 2)

    # Draw the text in the drop zone
    text_drop_rect = text_drop.get_rect(center=drop_zone_rect.center)
    window.blit(text_drop, text_drop_rect)

    # Draw the Select using file button
    pygame.draw.rect(window, select_using_color, select_using_file_rect,)
    pygame.draw.rect(window, boundry_color, select_using_file_rect, 2)

    #Draw the text in the Select Button
    text_select_rect = text_select.get_rect(center=select_using_file_rect.center)
    window.blit(text_select, text_select_rect)

    # Update the display
    pygame.display.update()
