from collections import deque

count_pumps = int(input())
pumps = deque()
start_position = 0
stops = 0
for _ in range(count_pumps):
    fuel, destination = input().split()
    pumps.append([int(fuel), int(destination)])

while stops < count_pumps:
    fuel = 0
    for i in range(count_pumps):
        fuel += pumps[i][0]
        destination = pumps[i][1]
        if fuel < destination:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= destination
        stops += 1

print(start_position)

# 3
# 1 5
# 10 3
# 3 4
