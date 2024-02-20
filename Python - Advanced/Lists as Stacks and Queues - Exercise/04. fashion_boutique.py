clothes = [int(x) for x in input().split()]
capacity_of_rack = int(input())

count_racks = 0

while clothes:
    count_racks += 1
    rack = capacity_of_rack
    while clothes and clothes[-1] <= rack:
        rack -= clothes.pop()
print(count_racks)

# 5 4 8 6 3 8 7 7 9
# 16

# 1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
# 20
