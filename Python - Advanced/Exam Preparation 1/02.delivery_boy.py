ROW, COl = [int(x) for x in input().split()]

matrix = []

position = []
is_delivered = False
for i in range(ROW):
    data = list(input())
    if 'B' in data:
        position = [i, data.index('B')]
    matrix.append(data)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
while True:
    command = input()
    if not command:
        break
    row = position[0] + directions[command][0]
    col = position[1] + directions[command][1]

    if 0 <= row < ROW and 0 <= col < COl:
        symbol = matrix[row][col]
        if symbol == '-':
            matrix[row][col] = '.'
        elif symbol == '*':
            continue
        elif symbol == 'P':
            matrix[row][col] = 'R'
            print("Pizza is collected. 10 minutes for delivery.")
        elif symbol == 'A':
            matrix[row][col] = 'P'
            is_delivered = True
            print("Pizza is delivered on time! Next order...")
            break
        position = [row, col]
    else:
        print("The delivery is late. Order is canceled.")
        break
if is_delivered:
    for x in matrix:
        print(''.join(x))
else:
    for i in range(len(matrix)):
        info = matrix[i]
        if 'B' in info:
            matrix[i][info.index('B')] = ' '
    for j in matrix:
        print(''.join(j))
