# from _collections import deque
#
# eggs = deque([int(x) for x in input().split(', ')])
# paper = [int(x) for x in input().split(', ')]
# filled_boxes = 0
#
# while eggs and paper:
#     cur_egg = eggs.popleft()
#     if cur_egg == 13:
#         paper[0], paper[-1] = paper[-1], paper[0]
#         continue
#     if cur_egg <= 0:
#         continue
#     cur_paper = paper.pop()
#     result = cur_egg + cur_paper
#     if result <= 50:
#         filled_boxes += 1
#     else:
#         continue
# if filled_boxes >= 1:
#     print(f"Great! You filled {filled_boxes} boxes.")
# else:
#     print("Sorry! You couldn't fill any boxes!")
# if eggs:
#     print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
# if paper:
#     print(f"Pieces of paper left: {', '.join(str(x) for x in paper)}")
from _collections import deque


class Eggs:
    def __init__(self, eggs, paper):
        self.eggs = eggs
        self.paper = paper
        self.filled_box = 0
        self.log = []

    def check_eggs(self):
        while self.eggs and self.paper:
            cur_egg = self.eggs.popleft()
            if cur_egg == 13:
                self.paper[0], self.paper[-1] = self.paper[-1], self.paper[0]
                continue
            if cur_egg <= 0:
                continue
            cur_paper = self.paper.pop()
            result = cur_egg + cur_paper
            if result <= 50:
                self.filled_box += 1
            else:
                continue

    def process_output(self):
        if self.filled_box >= 1:
            self.log.append(f"Great! You filled {self.filled_box} boxes.")
        else:
            self.log.append("Sorry! You couldn't fill any boxes!")
        if self.eggs:
            self.log.append(f"Eggs left: {', '.join(str(x) for x in self.eggs)}")
        if self.paper:
            self.log.append(f"Pieces of paper left: {', '.join(str(x) for x in self.paper)}")

    def __repr__(self):
        return '\n'.join(self.log)


eggs_size = deque(map(int, input().split(', ')))
paper_size = list(map(int, input().split(', ')))

output = Eggs(eggs_size, paper_size)
output.check_eggs()
output.process_output()
print(output)
