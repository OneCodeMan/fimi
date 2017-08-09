from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
import config
import os

# Action
i = 0
img_path = 'assets/img/stocksnap1/'
img_output = 'assets/img/stocksnapoutput1/'

# format: [font_type, font_size, font_color, quote]

for f in os.listdir(img_path):
    if f.endswith('.jpg'):
        for perm in config.permutations:
            img = Image.open(img_path + f)
            draw = ImageDraw.Draw(img)
            font_type = perm[0]
            font_size = perm[1]
            font_color = perm[2]
            quote = perm[3]

            img_width, img_height = img.size

            font = ImageFont.truetype('assets/fonts/' + font_type, font_size)

            lines = textwrap.wrap(quote, width=50)
            line_height = 0

            for line in lines:
                text_width, text_height = draw.textsize(line)
                x_text = ((img_width - text_width) / 4) - 70
                y_text = (img_height - text_height) / 4 + line_height
                
                draw.text((x_text, y_text), line, font_color, font=font)
                line_height += 40


            img.save(img_output + 'sample-out' + str(i) + '.jpg')
            i += 1
