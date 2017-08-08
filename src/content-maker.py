from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import config
import os

# Fonts
font_path = 'assets/font/Slabo27px-Regular.ttf'
font_size = 36

# Colors
colors = [(0, 0, 0)]

# Quote
quote = 'Be patient and tough; one day this pain will be useful to you.'

# Action
i = 0
img_path = 'assets/img/stocksnap1/'
img_output = 'assets/img/stocksnapoutput1/'

for f in os.listdir(img_path):
    if f.endswith('.jpg'):
        img = Image.open(img_path + f)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, font_size)
        draw.text((25, 100), quote, colors[0], font=font)
        img.save(img_output + 'sample-out' + str(i) + '.jpg')
        i += 1

'''
for each image:
    for each permutation (font type, size, color, position, quote):
        apply permutation to image
'''
