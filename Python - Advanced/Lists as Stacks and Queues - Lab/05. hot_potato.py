from collections import deque

names = deque(input().split())

rotation = int(input()) - 1

while len(names) != 1:
    names.rotate(-rotation)
    print(f'Removed {names.popleft()}')
print(f'Last is {names.popleft()}')

# Tracy Emily Daniel
# 2

# George Peter Michael William Thomas
# 10
