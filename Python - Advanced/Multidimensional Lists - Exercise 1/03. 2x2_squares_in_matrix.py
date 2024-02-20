rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for i in range(rows)]

count = 0
for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        if matrix[row_index][col_index] == matrix[row_index][col_index + 1] == matrix[row_index + 1][col_index] == \
                matrix[row_index + 1][col_index + 1]:
            count += 1
print(count)
# 3 4
# A B B D
# E B B B
# I J B B
