font_types = ['assets/font/Slabo27px-Regular.ttf'] # add more
font_sizes = [size for size in range(36, 62, 2)]
font_colors = [(0, 0, 0), (255, 255, 255)] # add more
text_positions = [(0, 0), (25, 25), (100, 100), (25, 100), (200, 200), (300, 300)] # add more

# Reading the quotes file
quotes_path = 'src/assets/text/quotes0.txt'
quotes_file_open = open(quotes_path, 'r')
quotes_file = quotes_file_open.read()
quotes_arr = quotes_file.split('\n')[:-1]


# Create permutation combos of 5
# format: [font_type, font_size, font_color, text_position, quote]
