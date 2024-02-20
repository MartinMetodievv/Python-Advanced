import os

WORKING_DIRECTION_PATH = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_DIRECTION_PATH, "SoftUni Python", "text.txt")

file = open(file_path, 'r')
file.close()
print(WORKING_DIRECTION_PATH)
