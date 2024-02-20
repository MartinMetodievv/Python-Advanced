text = tuple(input())

uniq = sorted(set(text))

for char in uniq:
    print(f'{char}: {text.count(char)} time/s')
