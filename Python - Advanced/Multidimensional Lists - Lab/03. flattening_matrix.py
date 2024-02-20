rows = int(input())

matrix = []

for i in range(rows):
    elements = [int(x) for x in input().split(', ')]
    matrix.append(elements)

flattened = []
for row_index in range(rows):
    for col_index in range(len(matrix[row_index])):
        flattened.append(matrix[row_index][col_index])
print(flattened)

# 2
# 1, 2, 3
# 4, 5, 6
