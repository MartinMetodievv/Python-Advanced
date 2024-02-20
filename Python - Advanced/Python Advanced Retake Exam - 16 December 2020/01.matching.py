from collections import deque

male = deque([int(x) for x in input().split()])
female = deque([int(x) for x in input().split()])
matching = 0

while male and female:
    cur_male = male.pop()
    if cur_male <= 0:
        continue

    if cur_male % 25 == 0:
        male.pop()
        continue

    cur_female = female.popleft()
    if cur_female <= 0:
        male.append(cur_male)
        continue
    
    if cur_female % 25 == 0:
        male.append(cur_male)
        female.popleft()
        continue
    if cur_male == cur_female:
        matching += 1
    else:
        male.append(cur_male - 2)
print(f'Matches: {matching}')

if male:
    print(f"Males left: {', '.join(str(x) for x in reversed(male))}")
else:
    print(f"Males left: none")

if female:
    print(f"Females left: {', '.join(str(x) for x in female)}")
else:
    print(f"Females left: none")
