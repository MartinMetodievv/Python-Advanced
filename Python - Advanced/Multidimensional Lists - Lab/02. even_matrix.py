rows = int(input())
matrix = []

for i in range(rows):
    elements = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    matrix.append(elements)
print(matrix)

# 2
# 1, 2, 3
# 4, 5, 6
