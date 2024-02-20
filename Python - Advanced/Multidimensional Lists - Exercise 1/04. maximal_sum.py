rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for row in range(rows)]

max_sum = {}

for i in range(rows - 2):
    for j in range(columns - 2):
        upper_left, upper_center, upper_right = matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]
        mid_left, mid_center, mid_right = matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]
        lower_left, lower_center, lower_right = matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]
        total_sum = sum([upper_left, upper_center, upper_right,
                         mid_left, mid_center, mid_right,
                         lower_left, lower_center, lower_right])
        if total_sum not in max_sum.keys():
            max_sum[total_sum] = [[upper_left, upper_center, upper_right],
                                  [mid_left, mid_center, mid_right],
                                  [lower_left, lower_center, lower_right]]

max_result = max(max_sum.keys())
print(f"Sum = {max_result}")
for row in max_sum[max_result]:
    print(*row)

# 4 5
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4
