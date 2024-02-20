n = int(input())

uniq = set()
for _ in range(n):
    data = input().split()
    for el in data:
        uniq.add(el)
print('\n'.join(uniq))

# 4
# Ce O
# Mo O Ce
# Ee
# Mo
