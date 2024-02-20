n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[j][n - j - 1] for j in range(n)]
difference = sum(primary_diagonal) - sum(secondary_diagonal)
print(abs(difference))
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
