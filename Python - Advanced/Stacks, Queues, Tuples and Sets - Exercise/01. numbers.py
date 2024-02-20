first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

n = int(input())

for _ in range(n):
    data = input().split()
    command = data[0]
    numbers = [int(i) for i in data[2:]]
    if command == 'Add':
        if data[1] == 'First':
            first_set.update(numbers)
        elif data[1] == 'Second':
            second_set.update(numbers)
    elif command == 'Remove':
        if data[1] == 'First':
            first_set.difference_update(numbers)
        elif data[1] == 'Second':
            second_set.difference_update(numbers)
    elif command + ' ' + data[1] == 'Check Subset':
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')

# 1 2 3 4 5
# 1 2 3
# 3
# Add First 5 6
# Remove Second 8 9 11
# Check Subset


# 5 4 2 9 9 5 4
# 1 1 1 5 6 5
# 4
# Add First 5 6 9 3
# Add Second 1 2 3 3 3
# Check Subset
# Remove Second 1 2 3 4 5
