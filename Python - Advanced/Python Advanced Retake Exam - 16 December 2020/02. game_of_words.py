# initial_string = input()
# size = int(input())
# field = []
# player_pos = []
#
# for i in range(size):
#     row = list(input())
#     field.append(row)
#     if "P" in row:
#         player_pos = [i, row.index("P")]
#
# nr_of_commands = int(input())
#
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1),
# }
#
# for _ in range(nr_of_commands):
#     command = input()
#     row, col = player_pos[0] + directions[command][0], player_pos[1] + directions[command][1]
#
#     if not 0 <= row < size or not 0 <= col < size:
#         initial_string = initial_string[:-1]
#         continue
#
#     if field[row][col] != "-":
#         initial_string += field[row][col]
#
#     field[player_pos[0]][player_pos[1]] = "-"
#     player_pos = [row, col]
#     field[row][col] = "P"
#
# print(initial_string)
# for row in field:
#     print(*row, sep="")
#
class WordsGame:

    def __init__(self, string, size):
        self.string = string
        self.size = size
        self.matrix = []
        self.my_pos = []
        self.moves = {'up': (-1, 0), 'down': (1, 0),
                      'left': (0, -1), 'right': (0, 1)}

    def create_game_field(self):
        for row in range(self.size):
            input_line = list(input())
            if 'P' in input_line:
                self.my_pos = [row, input_line.index('P')]
                input_line[self.my_pos[1]] = '-'
            self.matrix.append(input_line)

    def play_the_game(self, number):
        for _ in range(number):
            command = input()
            row = self.my_pos[0] + self.moves[command][0]
            col = self.my_pos[1] + self.moves[command][1]
            if 0 <= row < self.size and 0 <= col < self.size:
                symbol = self.matrix[row][col]
                if symbol != '-':
                    self.string += symbol
                    self.matrix[row][col] = '-'
                self.my_pos = [row, col]
            else:
                self.string = self.string[:len(self.string) - 1]
        self.matrix[self.my_pos[0]][self.my_pos[1]] = 'P'

    def __repr__(self):
        message = self.string
        message += '\n' + '\n'.join(''.join(row) for row in self.matrix)
        return message


initial_string = input()
size_of_matrix = int(input())

output = WordsGame(initial_string, size_of_matrix)
output.create_game_field()
output.play_the_game(int(input()))
print(output)

# Example_01
#
# Input
# Hello
# 4
# P---
# Mark
# -l-y
# --e-
# 4
# down
# right
# right
# right
#
# Output
# HelloMark
# ----
# ---P
# -l-y
# --e-
