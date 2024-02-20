ROWS, COLS = [int(x) for x in input().split(',')]

cheese_count = 0
eaten_cheese = 0
matrix = []
mouse_position = None


def valid_area(row, col):
    return 0 <= row < ROWS and 0 <= col < COLS


mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
for row_index in range(ROWS):
    data = list(input())
    if 'M' in data:
        mouse_position = [row_index, data.index('M')]
    cheese_count += data.count('C')
    matrix.append(data)

direction = input()
while direction != 'danger':
    cur_row, cur_col = mouse_position
    row_to_go, col_to_go = mapper[direction]
    desire_row = cur_row + row_to_go
    desire_col = cur_col + col_to_go

    if not valid_area(desire_row, desire_col):
        print("No more cheese for tonight!")
        break

    if matrix[desire_row][desire_col] == 'C':
        matrix[desire_row][desire_col] = 'M'
        mouse_position = [desire_row, desire_col]
        matrix[cur_row][cur_col] = '*'
        eaten_cheese += 1
        if eaten_cheese == cheese_count:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif matrix[desire_row][desire_col] == 'T':
        matrix[desire_row][desire_col] = 'M'
        matrix[cur_row][cur_col] = '*'
        print('Mouse is trapped!')
        break
    elif matrix[desire_row][desire_col] == '@':
        direction = input()
        continue
    else:
        matrix[desire_row][desire_col] = 'M'
        matrix[cur_row][cur_col] = '*'
        mouse_position = [desire_row, desire_col]
    direction = input()
if direction == 'danger':
    print("Mouse will come back later!")

for row in matrix:
    print(*row, sep='')

# 5,5
# **M**
# T@@**
# CC@**
# **@@*
# **CC*
# left
# down
# left
# down
# down
# down
# right
# danger
