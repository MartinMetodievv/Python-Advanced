from collections import deque

seats = input().split(', ')
first_sequence = deque([int(x) for x in input().split(', ')])
last_sequence = deque([int(x) for x in input().split(', ')])

rotations = 0
match_seat = []
while len(match_seat) < 3 and rotations != 10:
    first_num = first_sequence.popleft()
    second_num = last_sequence.pop()
    rotations += 1
    asc_value = chr(first_num + second_num)
    check_seat = str(first_num) + asc_value, str(second_num) + asc_value
    if check_seat[0] in seats or check_seat[1] in seats:
        if check_seat[0] not in match_seat or check_seat[1] not in match_seat:
            if check_seat[0] in seats:
                seats.remove(check_seat[0])
                match_seat.append(check_seat[0])
            if check_seat[1] in seats:
                seats.remove(check_seat[1])
                match_seat.append(check_seat[1])
        else:
            continue
    else:
        first_sequence.append(first_num)
        last_sequence.appendleft(second_num)
print(f"Seat matches: {', '.join(match_seat)}")
print(f"Rotations count: {rotations}")
