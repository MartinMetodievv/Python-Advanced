n = int(input())

matrix = []

for i in range(n):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)

sum_nums = 0
for row_index in range(n):
    sum_nums += matrix[row_index][row_index]
print(sum_nums)

# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# 3
# 1 2 3
# 4 5 6
# 7 8 9
