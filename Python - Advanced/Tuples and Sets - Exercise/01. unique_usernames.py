n = int(input())

uniq_names = set()
for _ in range(n):
    name = input()
    uniq_names.add(name)

print('\n'.join(uniq_names))

# 6
# George
# George
# George
# Peter
# George
# NiceGuy1234
