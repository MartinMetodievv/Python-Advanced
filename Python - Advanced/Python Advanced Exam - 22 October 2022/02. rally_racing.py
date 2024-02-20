# size = int(input())
# racing_number = input()
# kilometers_passed = 0
# is_reached = False
# player_pos = [0, 0]
# matrix = []
# tunnel = []
# for i in range(size):
#     data = input().split()
#     if 'T' in data:
#         tunnel.append([i, data.index('T')])
#     matrix.append(data)
# directions = {
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1),
# }
# while True:
#     command = input()
#     if command == 'End':
#         break
#     row = player_pos[0] + directions[command][0]
#     col = player_pos[1] + directions[command][1]
#     if 0 <= row < size and 0 <= col < len(matrix[row]):
#         symbol = matrix[row][col]
#         kilometers_passed += 10
#         player_pos = [row, col]
#         if symbol == 'F':
#             is_reached = True
#             break
#         elif symbol == 'T':
#             kilometers_passed += 20
#             if tunnel[0][0] == row and tunnel[0][1] == col:
#                 player_pos = [tunnel[1][0], tunnel[1][1]]
#             else:
#                 player_pos = [tunnel[0][0], tunnel[0][1]]
#             matrix[tunnel[0][0]][tunnel[0][1]] = '.'
#             matrix[tunnel[1][0]][tunnel[1][1]] = '.'
# matrix[player_pos[0]][player_pos[1]] = 'C'
# if is_reached:
#     print(f"Racing car {racing_number} finished the stage!")
# else:
#     print(f"Racing car {racing_number} DNF.")
#
# print(f"Distance covered {kilometers_passed} km.")
# for x in matrix:
#     print(''.join(x))
#
class CarRace:
    def __init__(self, size, race_number):
        self.size = size
        self.race_number = race_number
        self.kilometers_passed = 0
        self.is_reached = False
        self.player_pos = [0, 0]
        self.matrix = []
        self.tunnel = []
        self.directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1), }
        self.log = []

    def create_field(self):
        for i in range(self.size):
            data = input().split()
            if 'T' in data:
                self.tunnel.append([i, data.index('T')])
            self.matrix.append(data)

    def race(self):
        while True:
            command = input()
            if command == 'End':
                break
            row = self.player_pos[0] + self.directions[command][0]
            col = self.player_pos[1] + self.directions[command][1]
            if 0 <= row < self.size and 0 <= col < len(self.matrix[row]):
                symbol = self.matrix[row][col]
                self.kilometers_passed += 10
                self.player_pos = [row, col]
                if symbol == 'F':
                    self.is_reached = True
                    break
                elif symbol == 'T':
                    self.kilometers_passed += 20
                    if self.tunnel[0][0] == row and self.tunnel[0][1] == col:
                        self.player_pos = [self.tunnel[1][0], self.tunnel[1][1]]
                    else:
                        self.player_pos = [self.tunnel[0][0], self.tunnel[0][1]]
                    self.matrix[self.tunnel[0][0]][self.tunnel[0][1]] = '.'
                    self.matrix[self.tunnel[1][0]][self.tunnel[1][1]] = '.'
        self.matrix[self.player_pos[0]][self.player_pos[1]] = 'C'

    def print(self):
        if self.is_reached:
            self.log.append(f"Racing car {self.race_number} finished the stage!")
        else:
            self.log.append(f"Racing car {self.race_number} DNF.")
        self.log.append(f"Distance covered {self.kilometers_passed} km.")
        for x in self.matrix:
            self.log.append(''.join(x))

    def __repr__(self):
        return '\n'.join(self.log)


cur_size = int(input())
number = input()
output = CarRace(cur_size, number)
output.create_field()
output.race()
output.print()
print(output)
