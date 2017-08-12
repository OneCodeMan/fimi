import itertools
import os

# Image URLs
images_path = 'assets/text/imgurls0.txt'
images_path_open = open(images_path, 'r')
images_file = images_path_open.read()
image_links = images_file.split('\n')[:-1]

# Fonts
font_types = os.listdir('assets/fonts')
font_sizes = [size for size in range(38, 48, 2)]
font_colors = [(255, 255, 255), (0, 0, 0)]

# Reading the quotes file
quotes_path = 'assets/text/quotes0.txt'
quotes_file_open = open(quotes_path, 'r')
quotes_file = quotes_file_open.read()
quotes_arr = quotes_file.split('\n')[:-1]

quote_wraps = [wrap for wrap in range(30, 60, 10)]

# Create permutation combos of 5
# format: [font_type, font_size, font_color, quote, quote_wrap]
states = [font_types, font_sizes, font_colors, quotes_arr, quote_wraps]
permutations = list(itertools.product(*states))
