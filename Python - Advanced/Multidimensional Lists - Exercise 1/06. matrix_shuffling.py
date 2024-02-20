# def are_coordinates_valid(r1, c1, r2, c2, r, c):
#     return 0 <= r1 < r and 0 <= r2 < r and 0 <= c1 < c and 0 <= c2 < c
#
#
# rows, cols = [int(x) for x in input().split()]
# matrix = [[x for x in input().split()] for _ in range(rows)]
#
# while True:
#     data = input()
#     if data == 'END':
#         break
#     command = data.split()
#     if command[0] != 'swap' or len(command) != 5:
#         print('Invalid input')
#         continue
#
#     row1, col1, row2, col2 = [int(x) for x in command[1:]]
#
#     if are_coordinates_valid(row1, col1, row2, col2, rows, cols):
#         matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
#         [print(*row) for row in matrix]
#     else:
#         print('Invalid input')


rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for row in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break

    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue

    for i in range(1, 5):
        if command[i].isdigit():
            command[i] = int(command[i])
        else:
            print("Invalid input!")
            continue

    if command[1] < rows and command[2] < columns and command[3] < rows and command[4] < columns:
        matrix[command[1]][command[2]], matrix[command[3]][command[4]] = \
            matrix[command[3]][command[4]], matrix[command[1]][command[2]]
        for row in range(rows):
            print(*matrix[row])

    else:
        print("Invalid input!")
# 2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END

# 1 2
# Hello World
# 0 0 0 1
# swap 0 0 0 1
# swap 0 1 0 0
# END
