n = int(input())

cars = set()

for _ in range(n):
    command, number = input().split(', ')
    if command == 'IN':
        cars.add(number)
    elif command == 'OUT':
        # if number in cars:
        cars.remove(number)

if not cars:
    print("Parking Lot is Empty")
else:
    for x in cars:
        print(x)

# 10
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# IN, CA9999TT
# IN, CA2866HI
# OUT, CA1234TA
# IN, CA2844AA
# OUT, CA2866HI
# IN, CA9876HH
# IN, CA2822UU

# 4
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# OUT, CA1234TA
