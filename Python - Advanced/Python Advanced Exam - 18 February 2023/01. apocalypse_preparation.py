from collections import deque

textiles = deque([int(x) for x in input().split()])
medicament = [int(x) for x in input().split()]
healing_items = {'Patch': 0, 'Bandage': 0, 'MedKit': 0}

while True:
    if not textiles and not medicament:
        print("Textiles and medicaments are both empty.")
        break
    if not medicament:
        print("Medicaments are empty.")
        break
    if not textiles:
        print("Textiles are empty.")
        break
    cur_textile = textiles.popleft()
    cur_medicament = medicament.pop()
    result = cur_textile + cur_medicament
    if result == 30:
        healing_items['Patch'] += 1
    elif result == 40:
        healing_items['Bandage'] += 1
    elif result == 100:
        healing_items['MedKit'] += 1
    elif result > 100:
        healing_items['MedKit'] += 1
        result -= 100
        medicament[-1] += result

    else:
        cur_medicament += 10
        medicament.append(cur_medicament)
sorted_items = sorted(healing_items.items(), key=lambda x: (-x[1], x[0]))

for item in sorted_items:
    if int(item[1]) > 0:
        print(f'{item[0]} - {item[1]}')
if medicament:
    medicament.reverse()
    print(f"Medicaments left: {', '.join([str(x) for x in medicament])}")
if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
