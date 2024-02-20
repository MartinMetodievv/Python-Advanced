from collections import deque

fuel = [int(x) for x in input().split()]
additional_consumption = deque([int(x) for x in input().split()])
needed_fuel = deque([int(x) for x in input().split()])

final_print = []
reach_counter = 0
is_failed = False

while fuel and needed_fuel:
    cur_fuel = fuel.pop()
    cur_additional_consumption = additional_consumption.popleft()
    needed_gas = needed_fuel.popleft()
    result = cur_fuel - cur_additional_consumption
    reach_counter += 1
    if result >= needed_gas:
        print(f"John has reached: Altitude {reach_counter}")
        final_print.append(f"Altitude {reach_counter}")
    else:
        print(f"John did not reach: Altitude {reach_counter}")
        is_failed = True
        break

if final_print and is_failed:
    print(f"John failed to reach the top.\nReached altitudes: {', '.join(final_print)}")
elif not final_print and is_failed:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")
else:
    print("John has reached all the altitudes and managed to reach the top!")
