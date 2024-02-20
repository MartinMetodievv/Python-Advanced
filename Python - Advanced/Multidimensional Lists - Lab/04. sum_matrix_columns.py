rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for row_index in range(rows):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

for col_index in range(cols):
    sum_nums = 0
    for row in range(rows):
        sum_nums += matrix[row][col_index]
    print(sum_nums)
# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0
