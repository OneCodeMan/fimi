# Quotes on a black background and quotes on a white background

from PIL import Image, ImageFont, ImageDraw
import config
import textwrap
import uuid

white_rgb = (248, 248, 248)
white_path = 'assets/img/simplewhite1/'
black_font_color = (0, 0, 0)

black_rgb = (0, 1, 0)
black_path = 'assets/img/simpleblack1/'
white_font_color = (255, 255, 255)

img_width, img_height = (1200, 1200)
dim = (img_width, img_height)
font_size = 40
font_type = 'Merriweather-Bold.ttf'
line_break_width = 40

def make_simple(bg_color, text_color, path, img_name, font_type):
    for quote in config.quotes_arr:
        img_white = Image.new('RGBA', dim, bg_color)
        draw = ImageDraw.Draw(img_white)

        lines = textwrap.wrap(quote, width=line_break_width)
        font = ImageFont.truetype('assets/fonts/' + font_type, font_size)
        line_height = 0

        for line in lines:
            text_width, text_height = draw.textsize(line)
            x_text = ((img_width - text_width) / 6)
            y_text = ((img_height) / 3) + line_height

            draw.text((x_text, y_text), line, text_color, font=font)
            line_height += 50

        img_white.save(path + img_name + str(uuid.uuid4()) + '.png')


for font in config.font_types:
    make_simple(white_rgb, black_font_color, white_path, 'white', font)
    make_simple(black_rgb, white_font_color, black_path, 'black', font)
