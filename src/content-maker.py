from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
import config
import os
import uuid

# Directory behaviour
dir_exists = False
dir_version = 1

while not dir_exists:
	img_path = 'assets/img/stocksnap' + str(dir_version)
    img_output = 'assets/img/stocksnapoutput' + str(dir_version)

	if os.path.exists(img_path) and os.path.exists(img_output):
		dir_version += 1
	else:
		os.makedirs(img_path)
        os.makedirs(img_output)
		dir_exists = True

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


            img.save(img_output + 'sample-out' + str(uuid.uuid4()) + '.jpg')
