from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import config
import os

# Action
i = 0
img_path = 'assets/img/stocksnap1/'
img_output = 'assets/img/stocksnapoutput1/'

# format: [font_type, font_size, font_color, text_position, quote]

for f in os.listdir(img_path):
    if f.endswith('.jpg'):
        for perm in config.permutations:
            img = Image.open(img_path + f)
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('assets/fonts/' + perm[0], perm[1])
            draw.text(perm[3], perm[4], perm[2], font=font)
            img.save(img_output + 'sample-out' + str(i) + '.jpg')
            i += 1
