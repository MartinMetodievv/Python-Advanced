size = int(input())
directions = input().split(', ')

hazelnuts = 0
cur_row = 0
cur_col = 0

matrix = []

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 's':
            cur_row = row
            cur_col = col
for direction in directions:
    matrix[cur_row][cur_col] = '*'

    if direction == 'up':
        cur_row -= 1
    elif direction == 'down':
        cur_row += 1
    elif direction == 'left':
        cur_col -= 1
    elif direction == 'right':
        cur_col += 1

    if not (0 <= cur_row < size and 0 <= cur_col < size):
        print("The squirrel is out of the field.")
        break
    if matrix[cur_row][cur_col] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
    if matrix[cur_row][cur_col] == 'h':
        hazelnuts += 1
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break
else:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnuts}")

# 5
# left, left, up, right, up, up
# **h**
# t****
# *h***
# *h*s*ь
# *****
