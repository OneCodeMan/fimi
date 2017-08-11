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
font_size = 40
font_type = 'Bitter-Bold.ttf'
black_font_color = (0, 0, 0)
white_font_color = (255, 255, 255)
line_break_width = 40

# White
i = 0
for quote in config.quotes_arr:
    img_white = Image.new('RGBA', dim, white_rgb)
    draw = ImageDraw.Draw(img_white)

    lines = textwrap.wrap(quote, width=line_break_width)
    font = ImageFont.truetype('assets/fonts/' + font_type, font_size)
    line_height = 0

    for line in lines:
        text_width, text_height = draw.textsize(line)
        x_text = ((img_width - text_width) / 6)
        y_text = ((img_height) / 3) + line_height

        draw.text((x_text, y_text), line, black_font_color, font=font)
        line_height += 50

    img_white.save(white_path + 'white' + str(i) + '.png')
    i += 1


# Black
j = 0
for quote in config.quotes_arr:
    img_black = Image.new('RGBA', dim, black_rgb)
    draw = ImageDraw.Draw(img_black)

    lines = textwrap.wrap(quote, width=line_break_width)
    font = ImageFont.truetype('assets/fonts/' + font_type, font_size)
    line_height = 0

    for line in lines:
        text_width, text_height = draw.textsize(line)
        x_text = ((img_width - text_width) / 4)
        y_text = ((img_height - text_height) / 2) + line_height

        draw.text((x_text, y_text), line, white_font_color, font=font)
        line_height += 50

    img_black.save(black_path + 'black' + str(j) + '.png')
    j += 1
