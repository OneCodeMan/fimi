import itertools
import os

font_types = os.listdir('assets/fonts') # add more
font_sizes = [size for size in range(34, 38, 2)]
font_colors = [(255, 255, 255), (0, 0, 0)]

# Reading the quotes file
quotes_path = 'assets/text/quotes0.txt'
quotes_file_open = open(quotes_path, 'r')
quotes_file = quotes_file_open.read()
quotes_arr = quotes_file.split('\n')[:-1]


# Create permutation combos of 5
# format: [font_type, font_size, font_color, quote]
states = [font_types, font_sizes, font_colors, quotes_arr]
permutations = list(itertools.product(*states))
