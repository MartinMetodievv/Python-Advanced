number = int(input())
stack = []

for _ in range(number):
    data = input().split()
    command = data[0]
    if command == '1':
        stack.append(data[1])
    elif stack:
        if command == '2':
            stack.pop()
        elif command == '3':
            print(max(stack))
        elif command == '4':
            print(min(stack))
while stack:
    print(stack.pop(), end='')
    if stack:
        print(', ', end='')

# 9
# 1 97
# 2
# 1 20
# 2
# 1 26
# 1 20
# 3
# 1 91
# 4

# 10
# 2
# 1 47
# 1 66
# 1 32
# 4
# 3
# 1 25
# 1 16
# 1 8
# 4
