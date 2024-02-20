text = input().split('|')

matrix = []

for i in range(len(text) - 1, -1, -1):
    row = [int(x) for x in text[i].split()]
    if row:
        matrix.append(row)
for x in matrix:
    print(*x, sep=' ', end=' ')
