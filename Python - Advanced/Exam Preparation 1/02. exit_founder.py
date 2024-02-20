# from _collections import deque
#
# players = deque(input().split(', '))
# matrix = [[x for x in input().split()] for i in range(6)]
# rest = {'Tom': False, 'Jerry': False}
# directions = {
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1)
# }
# while True:
#     command = [int(x) for x in input() if x.isdigit()]
#     row, col = command[0], command[1]
#     cur_player = players.popleft()
#     players.append(cur_player)
#     if rest[cur_player]:
#         rest[cur_player] = False
#         continue
#     if matrix[row][col] == 'E':
#         print(f"{cur_player} found the Exit and wins the game!")
#         break
#     if matrix[row][col] == 'T':
#         print(f"{cur_player} is out of the game! The winner is {players[0]}.")
#         break
#     if matrix[row][col] == 'W':
#         print(f"{cur_player} hits a wall and needs to rest.")
#         rest[cur_player] = True
from _collections import deque


class ExitFounder:
    def __init__(self, players):
        self.players = players
        self.matrix = []
        self.directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
        self.rest = {'Tom': False, 'Jerry': False}
        self.size = 6
        self.log = []

    def create_field(self):
        self.matrix = [[x for x in input().split()] for i in range(self.size)]

    def try_to_find_exit(self):
        while True:
            command = [int(x) for x in input() if x.isdigit()]
            row, col = command[0], command[1]
            cur_player = self.players.popleft()
            self.players.append(cur_player)
            if self.rest[cur_player]:
                self.rest[cur_player] = False
                continue
            if self.matrix[row][col] == 'E':
                self.log.append(f"{cur_player} found the Exit and wins the game!")
                break
            if self.matrix[row][col] == 'T':
                self.log.append(f"{cur_player} is out of the game! The winner is {self.players[0]}.")
                break
            if self.matrix[row][col] == 'W':
                self.log.append(f"{cur_player} hits a wall and needs to rest.")
                self.rest[cur_player] = True

    def __repr__(self):
        return '\n'.join(self.log)


player = deque(input().split(', '))
output = ExitFounder(player)
output.create_field()
output.try_to_find_exit()
print(output)
