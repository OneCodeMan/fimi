# Quotes on a black background and quotes on a white background
from PIL import Image, ImageFont, ImageDraw

## TODO: don't make it completely black, or completely white

# White

img_white = Image.new('RGBA', (1200, 1200), 'white')
draw = ImageDraw.Draw(img_white)

img_white.save('white.png')

# Black

img_black = Image.new('RGBA', (1200, 1200), 'black')
draw = ImageDraw.Draw(img_black)

img_black.save('black.png')
