# Quotes on a black background and quotes on a white background

from PIL import Image, ImageFont, ImageDraw
import config
import textwrap

white_rgb = (248, 248, 248)
white_path = 'assets/img/simplewhite1/'
black_rgb = (0, 1, 0)
black_path = 'assets/img/simpleblack1/'
img_width, img_height = (1200, 1200)
dim = (img_width, img_height)
font_size = 36
font_type = 'NotoSans-Regular.ttf'
font_color = (0, 0, 0)

# White
i = 0
for quote in config.quotes_arr:
    img_white = Image.new('RGBA', dim, white_rgb)
    draw = ImageDraw.Draw(img_white)

    lines = textwrap.wrap(quote, width=50)
    font = ImageFont.truetype('assets/fonts/' + font_type, font_size)
    line_height = 0

    for line in lines:
        text_width, text_height = draw.textsize(line)
        x_text = ((img_width - text_width) / 4)
        y_text = ((img_height - text_height) / 2) + line_height

        draw.text((x_text, y_text), line, font_color, font=font)
        line_height += 50

    img_white.save(white_path + 'white' + str(i) + '.png')
    i += 1

# Black
'''
img_black = Image.new('RGBA', dim, black_rgb)
draw = ImageDraw.Draw(img_black)

img_black.save(black_path + 'black.png')
'''
