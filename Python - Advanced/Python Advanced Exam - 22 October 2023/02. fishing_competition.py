# size = int(input())
# passages = 0
# matrix = []
# my_position = []
# reach_passage = False
# is_fall = False
# for i in range(size):
#     data = list(input())
#     if 'S' in data:
#         my_position = [i, data.index('S')]
#     matrix.append(data)
#
# directions = {
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1),
# }
# while True:
#     command = input()
#     if command == "collect the nets":
#         break
#     row = my_position[0] + directions[command][0]
#     col = my_position[1] + directions[command][1]
#     if row < 0:
#         row = size - 1
#     elif row >= size:
#         row = 0
#     elif col < 0:
#         col = size - 1
#     elif col >= size:
#         col = 0
#
# if matrix[row][col].isdigit():
#     passages += int(matrix[row][col])
#     if passages >= 20:
#         reach_passage = True
#     matrix[row][col] = '-'
# elif matrix[row][col] == 'W':
#     is_fall = True
#     break
# matrix[my_position[0]][my_position[1]] = '-'
# my_position = [row, col]
# matrix[my_position[0]][my_position[1]] = 'S'
# if is_fall:
#     print(
#         f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{row},{col}]")
# else:
#     if not reach_passage:
#         lack_of_fish = 20 - passages
#         print(f"You didn't catch enough fish and didn't reach the quota! You need {lack_of_fish} tons of fish more.")
#     else:
#         print("Success! You managed to reach the quota!")
#     if passages > 0:
#         print(f"Amount of fish caught: {passages} tons.")
#     for row in matrix:
#         print(*row, sep='')

class Fishing:
    def __init__(self, size):
        self.size = size
        self.matrix = []
        self.my_position = []
        self.reach_passage = False
        self.is_fall = False
        self.passages = 0
        self.log = []
        self.directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1), }

    def create_game(self):
        for i in range(self.size):
            data = list(input())
            if 'S' in data:
                self.my_position = [i, data.index('S')]
            self.matrix.append(data)

    def check_row_col(self, row, col):
        if row < 0:
            row = self.size - 1
        elif row >= self.size:
            row = 0
        elif col < 0:
            col = self.size - 1
        elif col >= self.size:
            col = 0
        return row, col

    def check_ship(self):
        while True:
            command = input()
            if command == "collect the nets":
                break
            cur_row = self.my_position[0] + self.directions[command][0]
            cur_col = self.my_position[1] + self.directions[command][1]
            cur_row, cur_col = self.check_row_col(cur_row, cur_col)
            self.my_position.append([cur_row, cur_col])
            if self.matrix[cur_row][cur_col].isdigit():
                self.passages += int(self.matrix[cur_row][cur_col])
                if self.passages >= 20:
                    self.reach_passage = True
                self.matrix[cur_row][cur_col] = '-'
            elif self.matrix[cur_row][cur_col] == 'W':
                self.is_fall = True
                self.row = cur_row
                self.col = cur_col
                break
            self.matrix[self.my_position[0]][self.my_position[1]] = '-'
            self.my_position = [cur_row, cur_col]
            self.matrix[self.my_position[0]][self.my_position[1]] = 'S'

    def print_message(self):
        if self.is_fall:
            self.log.append(
                f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{self.row},{self.col}]")
        else:
            if not self.reach_passage:
                lack_of_fish = 20 - self.passages
                self.log.append(
                    f"You didn't catch enough fish and didn't reach the quota! You need {lack_of_fish} tons of fish more.")
            else:
                self.log.append("Success! You managed to reach the quota!")
            if self.passages > 0:
                self.log.append(f"Amount of fish caught: {self.passages} tons.")
            for row in self.matrix:
                self.log.append(''.join(row))

    def __repr__(self):
        return '\n'.join(self.log)


cur_size = int(input())
output = Fishing(cur_size)
output.create_game()
output.check_ship()
output.print_message()
print(output)
