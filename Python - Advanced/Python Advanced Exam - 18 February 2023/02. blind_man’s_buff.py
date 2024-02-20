ROWS, COLS = [int(x) for x in input().split()]

matrix = []
player_position = []
touched_people = 0
moves = 0

for x in range(ROWS):
    data = input().split()
    matrix.append(data)
    if 'B' in data:
        player_position = [x, data.index('B')]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    command = input()
    if command == 'Finish':
        break
    if touched_people == 3:
        break
    move_row, move_col = player_position[0] + directions[command][0], player_position[1] + directions[command][1]

    if 0 <= move_row < ROWS and 0 <= move_col < COLS:
        if matrix[move_row][move_col] != 'O':

            if matrix[move_row][move_col] == 'P':
                touched_people += 1
                moves += 1
            elif matrix[move_row][move_col] == '-':
                moves += 1
            matrix[player_position[0]][player_position[1]] = '-'
            matrix[move_row][move_col] = 'B'
            player_position = [move_row, move_col]
print("Game over!")
print(f"Touched opponents: {touched_people} Moves made: {moves}")
