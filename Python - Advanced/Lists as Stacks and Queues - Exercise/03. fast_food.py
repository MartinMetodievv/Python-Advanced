from collections import deque

quantity_food = int(input())
clients = deque(int(x) for x in input().split())

print(max(clients))
while clients and clients[0] <= quantity_food:
    quantity_food -= clients[0]
    clients.popleft()
if not clients:
    print('Orders complete')
else:
    print('Orders left:', end='')
    while clients:
        print(f' {clients.popleft()}', end='')
# 348
# 20 54 30 16 7 9

# 499
# 57 45 62 70 33 90 88 76 100 50
