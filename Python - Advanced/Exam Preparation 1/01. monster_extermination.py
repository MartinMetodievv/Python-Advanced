from collections import deque

monster_armor = deque([int(x) for x in input().split(',')])
knight = [int(x) for x in input().split(',')]

kills = 0

while monster_armor and knight:
    current_monster = monster_armor.popleft()
    current_knight = knight.pop()

    if current_knight >= current_monster:
        kills += 1
        current_knight -= current_monster
        if knight:
            knight[-1] += current_knight
        elif not knight and current_knight > 0:
            knight.append(current_knight)
    else:
        current_monster -= current_knight
        monster_armor.append(current_monster)

if not monster_armor:
    print("All monsters have been killed!")
if not knight:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {kills}")

# 20,15,10
# 5,15,10,25

# 30,25,40,35
# 15,20,10,30
