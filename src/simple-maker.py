# Quotes on a black background and quotes on a white background

from PIL import Image, ImageFont, ImageDraw
import config

white_rgb = (248, 248, 248)
white_path = 'assets/img/simplewhite1/'
black_rgb = (0, 1, 0)
black_path = 'assets/img/simpleblack1/'
dim = (1200, 1200)

# White
img_white = Image.new('RGBA', dim, white_rgb)
i = 0
for quote in config.quotes_arr:
    draw = ImageDraw.Draw(img_white)

    img_white.save(white_path + 'white' + str(i) + '.png')

    i += 1

# Black
'''
img_black = Image.new('RGBA', dim, black_rgb)
draw = ImageDraw.Draw(img_black)

img_black.save(black_path + 'black.png')
'''
