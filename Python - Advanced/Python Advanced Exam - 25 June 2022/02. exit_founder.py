from collections import deque

names = deque(input().split(', '))
matrix = [[x for x in input().split()] for i in range(6)]

suspended = {'Tom': False, 'Jerry': False}
while True:
    current_player = names.popleft()
    names.append(current_player)

    move_to_pos = tuple(int(x) for x in list(input()) if x.isdigit())
    if suspended[current_player]:
        suspended[current_player] = False
        continue
    if matrix[move_to_pos[0]][move_to_pos[1]] == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif matrix[move_to_pos[0]][move_to_pos[1]] == 'T':
        print(f"{current_player} is out of the game! The winner is {names.popleft()}.")
        break
    elif matrix[move_to_pos[0]][move_to_pos[1]] == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        suspended[current_player] = True
