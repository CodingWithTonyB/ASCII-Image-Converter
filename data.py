import datetime
import os

#UI.py variables
# Set up the window
win_width = 500
win_height = 700

#Colors
WHITE = (255,255,255)
BUTTON_GRAY = (150,150,150)
BUTTON_LIGHT_GRAY = (130,130,130)

# Save the file as date & time.png
timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
output_filename = f"output_{timestamp}.png"
output_path = os.path.join(r"C:\Users\Crypt\Documents\Code\ASCII\ASCII-Image-Converter\outputs/", output_filename)

# Set up the allowed file extensions
allowed_extensions = [".jpg", ".png"]




#ASCII.py variables:
#scale factor
scaleFactor = 0.2

#brightness
'''0 is regular for brightness 
 adding brightness just increases 
 the r g b by the ammount'''
brightness = 30
#Char Lenth
oneCharWidth = 10
oneCharHeight = 16

#charachters
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
# chars = "#Wo- "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

#starts the loop sequence
looped = 1
