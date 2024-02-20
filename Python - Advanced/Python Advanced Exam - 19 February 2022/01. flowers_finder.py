from _collections import deque

vowels = deque(input().split())
consonants = input().split()
searched_word = ["rose", "tulip", "lotus", "daffodil"]
is_found = False

founded_word = {}
while vowels and consonants and not is_found:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    for word in searched_word:
        if word not in founded_word:
            founded_word[word] = [[]] * len(word)
        if vowel or consonant in word:
            for index, letter in enumerate(word):
                if vowel == letter:
                    founded_word[word][index] = vowel
                if consonant == letter:
                    founded_word[word][index] = consonant
        data = f'{"".join(map(str, founded_word[word]))}'
        if word == data:
            is_found = True
            break
if is_found:
    print(f'Word found: {word}')
else:
    print('Cannot find any word!')
if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(consonants)} ')
# from collections import deque
#
# vowels = deque(input().split())
# consonants = input().split()
# searched_word = ["rose", "tulip", "lotus", "daffodil"]
#
# founded_word = {}
#
# success = False
#
# while vowels and consonants and not success:
#     vowel = vowels.popleft() if vowels else ''
#     consonant = consonants.pop() if consonants else ''
#     for word in searched_word:
#         if word not in founded_word:
#             founded_word[word] = [[]] * len(word)
#         if vowel or consonant in word:
#             for index, letter in enumerate(word):
#                 if vowel == letter:
#                     founded_word[word][index] = vowel
#                 if consonant == letter:
#                     founded_word[word][index] = consonant
#         if word == f'{"".join(map(str, founded_word[word]))}':
#             success = True
#             break
# #
# if success:
#     print(f'Word found: {word}')
# else:
#     print('Cannot find any word!')
# if vowels:
#     print(f'Vowels left: {" ".join(vowels)}')
# if consonants:
#     print(f'Consonants left: {" ".join(consonants)} ')
