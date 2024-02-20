rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for row in range(rows):
    elements = [int(x) for x in input().split(', ')]
    matrix.append(elements)
max_sum = 0
max_sum_sub_matrix = []
for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        first_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        down_element = matrix[row_index + 1][col_index]
        diagonal_element = matrix[row_index + 1][col_index + 1]
        sum_elements = first_element + next_element + diagonal_element + down_element

        if max_sum < sum_elements:
            max_sum = sum_elements
            max_sum_sub_matrix = [[first_element, next_element], [down_element, diagonal_element]]
print(*max_sum_sub_matrix[0])
print(*max_sum_sub_matrix[1])
print(max_sum)

# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
