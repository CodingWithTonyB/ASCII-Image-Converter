from PIL import Image, ImageDraw, ImageFont
from data import(output_path, charArray, interval,
                scaleFactor, brightness, oneCharHeight,
                oneCharWidth, looped)
import math
import os

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

def runASCII(path):
    global looped
    print('Conversion Started')
    text_file = open(r"ASCII\ASCII-Image-Converter\Output.txt", "w")

    im = Image.open(path)

    fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

    width, height = im.size
    im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
    width, height = im.size
    pix = im.load()

    outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
    d = ImageDraw.Draw(outputImage)

    for i in range(height):
        for j in range(width):
            #print(updated_loop, " out of ", width*height, " done")
            r, g, b = pix[j, i]
            h = int(r/3 + g/3 + b/3)
            pix[j, i] = (h, h, h)
            text_file.write(getChar(h))
            d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r+brightness, g+brightness, b+brightness))
            updated_loop = looped+1
            
        text_file.write('\n')

    outputImage.save(output_path)

    os.startfile(output_path)

    print('conversion finished')
