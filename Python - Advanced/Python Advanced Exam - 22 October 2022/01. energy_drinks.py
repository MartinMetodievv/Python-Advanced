from collections import deque

miligrams_of_caffeine = deque([int(x) for x in input().split(', ')])
drinks = deque([int(x) for x in input().split(', ')])

miligrams_per_night = 300
stamat_total_caffeine = 0
while miligrams_of_caffeine and drinks:
    cur_mil = miligrams_of_caffeine.pop()
    cur_drink = drinks.popleft()
    result = cur_mil * cur_drink
    if (stamat_total_caffeine + result) <= miligrams_per_night:
        stamat_total_caffeine += result
    elif (stamat_total_caffeine + result) > miligrams_per_night:
        drinks.append(cur_drink)
        if stamat_total_caffeine != 0:
            stamat_total_caffeine -= 30
if drinks:
    print(f"Drinks left: {', '.join([str(x) for x in drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {stamat_total_caffeine} mg caffeine.")
