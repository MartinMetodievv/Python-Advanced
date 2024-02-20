from collections import deque

stack = deque()
while True:
    names = input()
    if names == 'End':
        break
    if names == 'Paid':
        while stack:
            print(stack.popleft())
    else:
        stack.append(names)

print(f'{len(stack)} people remaining.')
