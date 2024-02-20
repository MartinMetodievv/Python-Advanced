n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command = input().split()
    if command[0] == 'END':
        break
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])
    if row < 0 or row >= n or col < 0 or col >= n:
        print("Invalid coordinates")
        continue

    if command[0] == 'Add':
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

for matrix_row in matrix:
    print(*matrix_row, sep=' ')
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END
