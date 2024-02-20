n = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
# matrix = []
# for _ in range(n):
#     sub_mat = []
#     for x in input().split(', '):
#         sub_mat.append(int(x))
#     matrix.append(sub_mat)

primary_diagonal = [matrix[i][i] for i in range(n)]
second_diagonal = [matrix[j][n - j - 1] for j in range(n)]
# right_down = []
# for i in range(n):
#     first_diagonal = matrix[i][i]
#     right_down.append(first_diagonal)
# left_down = []
# for j in range(n):
#     second_diagonal = matrix[j][n - j - 1]
#     left_down.append(second_diagonal)
print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in second_diagonal])}. Sum: {sum(second_diagonal)}")
# 3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
