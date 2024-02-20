rows, cols = [int(x) for x in input().split()]

matrix = []

for r in range(rows):
    sub_matrix = []
    for c in range(cols):
        sub_matrix.append(chr(97 + r) + chr(97 + r + c) + chr(97 + r))
    matrix.append(sub_matrix)

for i in range(rows):
    print(*matrix[i])
