n = int(input())

matrix = []
submarine_position = []
hits = 3
cruises = 0

for i in range(n):
    data = list(input())
    if 'S' in data:
        submarine_position = [i, data.index('S')]
    cruises += data.count('C')
    matrix.append(data)
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while cruises > 0 or hits > 0:
    command = input()
    row, col = submarine_position[0] + directions[command][0], submarine_position[1] + directions[command][1]

    if matrix[row][col] == '*':
        matrix[row][col] = 'S'
        matrix[submarine_position[0]][submarine_position[1]] = '-'
        hits -= 1
        if hits == 0:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
            break
    if matrix[row][col] == '-':
        matrix[row][col] = 'S'
        matrix[submarine_position[0]][submarine_position[1]] = '-'

    if matrix[row][col] == 'C':
        matrix[row][col] = 'S'
        matrix[submarine_position[0]][submarine_position[1]] = '-'
        cruises -= 1
        if cruises == 0:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break
    submarine_position = [row, col]
for row in matrix:
    print(''.join(row))
