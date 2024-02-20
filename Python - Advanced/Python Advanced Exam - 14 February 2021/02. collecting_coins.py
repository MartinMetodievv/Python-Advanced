from math import floor

size = int(input())

matrix = []
coins = 0
path = []
for i in range(size):
    data = input().split()
    if 'P' in data:
        path.append([i, data.index('P')])
        data[path[-1][1]] = 'v'
    matrix.append(data)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    command = input()
    if not command:
        break

    row, col = path[-1][0] + directions[command][0], path[-1][1] + directions[command][1]
    if 0 <= row < size or 0 <= col < size:
        if row >= size:
            row = 0
        elif row < 0:
            row = size - 1
        elif col >= size:
            col = 0
        elif col < 0:
            col = size - 1
    path.append([row, col])
    symbol = matrix[row][col]
    if symbol == 'X':
        coins = floor(coins / 2)
        break
    elif symbol.isdigit():
        coins += int(symbol)
        matrix[row][col] = 'v'

    if coins >= 100:
        break

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print("Your path:")
for row in path:
    print(row, sep='\n')
##################################### variant 01 #####################################
# from math import floor
#
# size = int(input())
#
# moves = {"up": (-1, 0), "down": (1, 0),
#          "left": (0, -1), "right": (0, 1)}
#
# game_field = []
# player_pos = []
# path = []
#
# collected_coins = 0
# for row in range(size):
#     input_line = input().split()
#     if 'P' in input_line:
#         player_pos.append([row, input_line.index('P')])
#         input_line[player_pos[-1][1]] = 'v'
#     game_field.append(input_line)
#
# while True:
#     command = input()
#     if not command:
#         break
#
#     row, col = player_pos[-1][0] + moves[command][0], player_pos[-1][1] + moves[command][1]
#
#     if row >= size:
#         row = 0
#     elif row < 0:
#         row = size - 1
#     elif col >= size:
#         col = 0
#     elif col < 0:
#         col = size - 1
#     player_pos.append([row, col])
#
#     symbol = game_field[row][col]
#     if symbol == 'X':
#         collected_coins = floor(collected_coins / 2)
#         break
#     elif symbol.isdigit():
#         collected_coins += int(symbol)
#         game_field[row][col] = 'v'
#
#     if collected_coins >= 100:
#         break
#
# if collected_coins >= 100:
#     print(f"You won! You've collected {collected_coins} coins.")
# else:
#     print(f"Game over! You've collected {collected_coins} coins.")
# print('Your path:')
# print(*player_pos, sep='\n')
from math import floor


class CollectingCoins:

    def __init__(self, size):
        self.size = size
        self.moves = {"up": (-1, 0), "down": (1, 0),
                      "left": (0, -1), "right": (0, 1)}
        self.game_field = []
        self.player_pos = []
        self.collected_coins = 0
        self.log = ''

    def create_game_field(self):
        for row in range(self.size):
            input_line = input().split()
            if 'P' in input_line:
                self.player_pos.append([row, input_line.index('P')])
                input_line[self.player_pos[-1][1]] = 'v'
            self.game_field.append(input_line)

    def check_row_col(self, row, col):
        if row >= self.size:
            row = 0
        elif row < 0:
            row = self.size - 1
        elif col >= self.size:
            col = 0
        elif col < 0:
            col = self.size - 1
        return row, col

    def collect_the_coins(self):
        while True:
            command = input()
            if not command:
                break

            row = self.player_pos[-1][0] + self.moves[command][0]
            col = self.player_pos[-1][1] + self.moves[command][1]
            row, col = self.check_row_col(row, col)
            self.player_pos.append([row, col])

            symbol = self.game_field[row][col]
            if symbol == 'X':
                self.collected_coins = floor(self.collected_coins / 2)
                break
            elif symbol.isdigit():
                self.collected_coins += int(symbol)
                self.game_field[row][col] = 'v'

            if self.collected_coins >= 100:
                break

    def prepare_result(self):
        if self.collected_coins >= 100:
            self.log = f"You won! You've collected {self.collected_coins} coins."
        else:
            self.log = f"Game over! You've collected {self.collected_coins} coins."
        self.log += '\nYour path:'
        self.log += '\n' + '\n'.join(str(row) for row in self.player_pos)

    def __repr__(self):
        return f'{self.log}'


size_of_field = int(input())

output = CollectingCoins(size_of_field)
output.create_game_field()
output.collect_the_coins()
output.prepare_result()
print(output)
