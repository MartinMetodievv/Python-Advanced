import os

WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath((__file__)))
file_path = os.path.join(WORKING_DIRECTORY_PATH, 'text.txt')

file = open(file_path, 'r')
total = 0

for el in file:
    total += int(el)
file.close()
print(total)
