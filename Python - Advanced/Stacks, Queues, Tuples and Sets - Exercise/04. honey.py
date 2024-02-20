from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

functions_dict = {
    "+": lambda x, y: abs(x + y),
    "-": lambda x, y: abs(x - y),
    "*": lambda x, y: abs(x * y),
    "/": lambda x, y: abs(x / y)}

collected_honey = 0
while bees and nectar:
    first_bee = bees.popleft()
    last_nectar = nectar.pop()
    if last_nectar == first_bee and last_nectar == 0:
        continue
    if first_bee > last_nectar:
        bees.appendleft(first_bee)
        continue
    else:
        symbol = symbols.popleft()
        collected_honey += functions_dict[symbol](first_bee, last_nectar)
print(f'Total honey made: {collected_honey}')
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
# 20 62 99 35 0 150
# 120 60 10 1 70 10
# + / * - - /

# 30
# 15 9 5 150 8
# * + + *
from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
total_honey = 0

# functions_dict = {
#     "+": lambda x, y: abs(x + y),
#     "-": lambda x, y: abs(x - y),
#     "*": lambda x, y: abs(x * y),
#     "/": lambda x, y: abs(x / y)
# }

while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()
    if current_nectar == current_bee and current_nectar == 0:
        continue

    if current_bee > current_nectar:
        working_bees.appendleft(current_bee)
        continue

    else:
        current_symbol = symbols.popleft()
        total_honey += functions_dict[current_symbol](current_bee, current_nectar)

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
