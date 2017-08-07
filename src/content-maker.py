from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os

# Fonts
font_path = 'assets/font/Slabo27px-Regular.ttf'
font_size = 36

# Quote
quote = 'Be patient and tough; one day this pain will be useful to you.'

# Reading the quotes file
quotes_path = 'assets/text/quotes0.txt'
quotes_file_open = open(quotes_path, 'r')
quotes_file = quotes_file_open.read()
quotes_arr = quotes_file.split('\n')[:-1]

# Action
i = 0
img_path = 'assets/img/stocksnap1/'
img_output = 'assets/img/stocksnapoutput1/'
for f in os.listdir(img_path):
    if f.endswith('.jpg'):
        img = Image.open(img_path + f)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, font_size)
        draw.text((25, 100), quote, (0, 0, 0), font=font)
        img.save(img_output + 'sample-out' + str(i) + '.jpg')
        i += 1
