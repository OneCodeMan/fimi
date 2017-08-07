
# Reading the quotes file

path = 'assets/text/quotes0.txt'
quotes_file_open = open(path, 'r')
quotes_file = quotes_file_open.read()
quotes_arr = quotes_file.split('\n')[:-1]

# 
