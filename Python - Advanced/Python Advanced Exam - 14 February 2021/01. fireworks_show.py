from _collections import deque

fireworks_effects = deque(int(x) for x in input().split(', '))
power = deque(int(x) for x in input().split(', '))
is_prepared = False
firework = {'Palm Fireworks': 0, 'Willow Fireworks': 0, 'Crossette Fireworks': 0}
while fireworks_effects and power:
    cur_firework = fireworks_effects.popleft()
    if cur_firework <= 0:
        continue
    cur_power = power.pop()
    if cur_power <= 0:
        fireworks_effects.appendleft(cur_firework)
        continue
    result = cur_firework + cur_power
    if result % 3 == 0 and result % 5 != 0:
        firework['Palm Fireworks'] += 1
    elif result % 5 == 0 and result % 3 != 0:
        firework['Willow Fireworks'] += 1
    elif result % 3 == 0 and result % 5 == 0:
        firework['Crossette Fireworks'] += 1
    else:
        cur_firework -= 1
        fireworks_effects.append(cur_firework)
        power.append(cur_power)
    if firework['Palm Fireworks'] == 3 and firework['Willow Fireworks'] >= 3 and firework['Crossette Fireworks'] >= 3:
        is_prepared = True
        break

if is_prepared:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in fireworks_effects)}")
if power:
    print(f"Explosive Power left: {', '.join(str(x) for x in power)}")

result = ''
for k, v in firework.items():
    result += f'{k}: {v}\n'
print(result)
