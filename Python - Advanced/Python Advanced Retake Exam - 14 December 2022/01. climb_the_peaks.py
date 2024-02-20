from collections import deque

food_supplies = [int(x) for x in input().split(', ')]
daily_stamina = deque([int(x) for x in input().split(', ')])
conquered_peaks = []
peaks = deque([["Vihren", 80],
               ["Kutelo", 90],
               ["Banski Suhodol", 100],
               ["Polezhan", 60],
               ["Kamenitza", 70],
               ])
for i in range(7):
    while food_supplies and daily_stamina and peaks:
        cur_food = food_supplies.pop()
        cur_stamina = daily_stamina.popleft()
        result = cur_food + cur_stamina
        if result >= peaks[0][1]:
            conquered_peaks.append(peaks[0][0])
            peaks.popleft()
        else:
            break
