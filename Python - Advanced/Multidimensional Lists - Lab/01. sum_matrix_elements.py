data = input().split(', ')
rows = int(data[0])
cols = int(data[1])
matrix = []
sum_nums = 0
for i in range(rows):
    elements = [int(x) for x in input().split(', ')]
    sum_nums += sum(elements)
    matrix.append(elements)
print(sum_nums)
print(matrix)

# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
