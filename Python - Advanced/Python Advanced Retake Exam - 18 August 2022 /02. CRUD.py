rows = 6
cols = 6

matrix = []
for i in range(rows):
    matrix.append(input().split())
position = input()

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
starting_position = [int(x) for x in position if x.isdigit()]

while True:
    command = input()
    data = command.split(", ")
    action = data[0]

    if action == 'Stop':
        break
    direction = data[1]
    row, col = starting_position[0] + directions[direction][0], starting_position[1] + directions[direction][1]

    if action == 'Create':
        if matrix[row][col] == ".":
            matrix[row][col] = data[2]
    elif action == 'Update':
        if matrix[row][col].isalnum():
            matrix[row][col] = data[2]
    elif action == 'Delete':
        if matrix[row][col].isalnum():
            matrix[row][col] = "."
    elif action == 'Read':
        if matrix[row][col] != ".":
            print(matrix[row][col])
    starting_position = [row, col]

for row in matrix:
    print(*row)
