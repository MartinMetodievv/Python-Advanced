def words_sorting(*args):
    words = {}
    result = ''
    for word in args:
        if word not in words:
            words[word] = 0
        for letter in word:
            words[word] += ord(letter)
    total_value = sum([x for x in words.values()])
    if total_value % 2 == 0:
        sorted_words = dict(sorted(words.items(), key=lambda x: x[0]))
    elif total_value % 2 != 0:
        sorted_words = dict(sorted(words.items(), key=lambda x: (-x[1])))
    for k, v in sorted_words.items():
        result += f'{k} - {v}\n'
    return result


#
# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#     ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))

# print(
#     words_sorting(
#         'cacophony',
#         'accolade'
#     ))
