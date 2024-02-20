from collections import deque

colors = deque(input().split())
main_colors = ['red', 'blue', 'yellow']
secondary_color = {'orange': ['red', 'yellow'],
                   'purple': ['red', 'blue'],
                   'green': ['blue', 'yellow']}

collected_colors = []

while colors:
    first_str = colors.popleft()
    last_str = colors.pop() if colors else ''
    if first_str + last_str in main_colors or first_str + last_str in secondary_color:
        collected_colors.append(first_str + last_str)
    elif last_str + first_str in main_colors or last_str + first_str in secondary_color:
        collected_colors.append(last_str + first_str)
    else:
        if len(first_str) > 1:
            colors.insert(len(colors) // 2, first_str[:-1])
        if len(last_str) > 1:
            colors.insert(len(colors) // 2, last_str[:-1])

for color in collected_colors:
    if color in secondary_color:
        for el in secondary_color[color]:
            if el not in collected_colors:
                collected_colors.remove(color)
                break
print(collected_colors)
