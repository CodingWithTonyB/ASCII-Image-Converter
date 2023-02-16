import pygame
import os
import tkinter as tk
from tkinter import filedialog
from ASCII import runASCII
from data import (output_path, WHITE, BUTTON_GRAY,
            BUTTON_LIGHT_GRAY, allowed_extensions,
            win_width, win_height, looped)

pygame.init()

rect_start_x = 15
rect_start_y = 50

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Image to ASCII converter")


#Image Variables
loaded = False

# Set up font and text
font = pygame.font.Font(None, 30)
font_select = pygame.font.Font(None, 15)
text_drop = font.render("Drop a photo here", True, WHITE)
text_select = font_select.render("Select File", True, WHITE)

# Set up the allowed file extensions
allowed_extensions = [".jpg", ".png"]

# Set up the loading bar
loading_bar_rect = pygame.Rect(15, 10, win_width-30, 10)
loading_bar_color = (255, 165, 0) # Orange color
loading_bar_progress = 0.0 # Initialize progress to 0%

def handleError():
    print('invalid file type')

# Define a function to handle dropping files
def handle_drop_file(file_path):
    # Check if the dropped file has an allowed extension
    if os.path.splitext(file_path)[1] in allowed_extensions:
        print("File dropped:", file_path)
        runASCII(file_path)
        print(looped, " out of done")
    else:
        handleError()


# Set up the button to select using file
select_using_file_rect = pygame.Rect(15,10,80,30)
select_using_color = BUTTON_LIGHT_GRAY
select_using_highlight_color = BUTTON_GRAY

# Set up the drop zone rectangle
drop_zone_rect = pygame.Rect(15, 50, 
                             win_width-30, 
                             win_height-60)
drop_zone_color = BUTTON_LIGHT_GRAY
drop_zone_highlight_color = BUTTON_GRAY

# Main game loop
def runUI():
    global drop_zone_rect, drop_zone_color, drop_zone_highlight_color
    global select_using_color, select_using_file_rect, select_using_highlight_color
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
                    drop_zone_color = BUTTON_LIGHT_GRAY
            if event.type == pygame.MOUSEMOTION:
                if select_using_file_rect.collidepoint(event.pos):
                    select_using_color = select_using_highlight_color
                else:
                    select_using_color = BUTTON_LIGHT_GRAY
            # Handle user events
            if event.type == pygame.USEREVENT:
                window.fill((0, 0, 0))

        # Clear the screen
        window.fill((100, 100, 100))
        boundry_color = (170,170,170)
        # Draw the drop zone rectangle
        pygame.draw.rect(window, drop_zone_color, drop_zone_rect)
        pygame.draw.rect(window, boundry_color, drop_zone_rect, 1)

        # Draw the text in the drop zone
        text_drop_rect = text_drop.get_rect(center=drop_zone_rect.center)
        window.blit(text_drop, text_drop_rect)

        # Draw the Select using file button
        pygame.draw.rect(window, select_using_color, select_using_file_rect,)
        pygame.draw.rect(window, boundry_color, select_using_file_rect, 1)

        #Draw the text in the Select Button
        text_select_rect = text_select.get_rect(center=select_using_file_rect.center)
        window.blit(text_select, text_select_rect)

        # Update the display
        pygame.display.update()
