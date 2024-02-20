from collections import deque

quantity_of_water = int(input())
list_of_names = deque()
while True:
    names = input()
    if names == 'Start':
        break
    list_of_names.append(names)

while True:
    command = input().split()
    if command[0].isdigit():
        liters = int(command[0])
        if liters <= quantity_of_water:
            print(f'{list_of_names.popleft()} got water')
            quantity_of_water -= liters
        else:
            print(f'{list_of_names.popleft()} must wait')
    elif len(command) > 1:
        data = int(command[1])
        quantity_of_water += data
    elif command[0] == 'End':
        print(f'{quantity_of_water} liters left')
        break
# 2
# Peter
# Amy
# Start
# 2
# refill 1
# 1
# End


# 10
# Peter
# George
# Amy
# Alice
# Start
# 2
# 3
# 3
# 3
# End