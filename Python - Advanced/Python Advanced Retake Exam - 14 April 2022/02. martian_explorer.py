# size = 6
#
# matrix = []
# position = []
# deposits = {'M': 'Metal', 'W': 'Water', 'C': 'Concrete'}
# found_deposit = set()
#
# for i in range(size):
#     data = input().split()
#     if 'E' in data:
#         position = [i, data.index('E')]
#     matrix.append(data)
#
# directions = {
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1)
# }
# command = input().split(', ')
# for direction in command:
#     row = position[0] + directions[direction][0]
#     col = position[1] + directions[direction][1]
#
#     if row < 0:
#         row = len(matrix) - 1
#     elif row == len(matrix):
#         row = 0
#     elif col < 0:
#         col = len(matrix) - 1
#     elif col == len(matrix):
#         col = 0
#     symbol = matrix[row][col]
#     if symbol in deposits:
#         material = deposits[symbol]
#         found_deposit.add(material)
#         print(f"{material} deposit found at ({row}, {col})")
#     elif symbol == 'R':
#         print(f"Rover got broken at ({row}, {col})")
#         break
#     position = [row, col]
# if len(found_deposit) < 3:
#     print("Area not suitable to start the colony.")
# else:
#     print("Area suitable to start the colony.")

class MartianExplorer:
    def __init__(self, size):
        self.size = size
        self.matrix = []
        self.position = []
        self.directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
        self.deposits = {'M': 'Metal', 'W': 'Water', 'C': 'Concrete'}
        self.founded_deposits = set()
        self.command_line = []
        self.log = []

    def map(self):
        for i in range(self.size):
            data = input().split()
            if 'E' in data:
                self.position = [i, data.index('E')]
            self.matrix.append(data)

    def create_command_line(self):
        for command in input().split(', '):
            self.command_line.append(command)

    def searching_resourse(self):
        def check_location(row, col):
            if row < 0:
                row = self.size - 1
            elif row == self.size:
                row = 0
            elif col < 0:
                col = self.size - 1
            elif col == self.size:
                col = 0
            return row, col

        for directon in self.command_line:
            rover_row = self.position[0] + self.directions[directon][0]
            rover_col = self.position[1] + self.directions[directon][1]
            rover_row, rover_col = check_location(rover_row, rover_col)
            symbol = self.matrix[rover_row][rover_col]
            if symbol in self.deposits:
                material = self.deposits[symbol]
                self.founded_deposits.add(material)
                self.log.append(f"{material} deposit found at ({rover_row}, {rover_col})")
            elif symbol == 'R':
                self.log.append(f"Rover got broken at ({rover_row}, {rover_col})")
                break
            self.position = [rover_row, rover_col]

    def __repr__(self):
        if len(self.founded_deposits) < 3:
            self.log.append("Area not suitable to start the colony.")
        else:
            self.log.append("Area suitable to start the colony.")
        return '\n'.join(self.log)


size_matrix = 6
output = MartianExplorer(size_matrix)
output.map()
output.create_command_line()
output.searching_resourse()
print(output)
