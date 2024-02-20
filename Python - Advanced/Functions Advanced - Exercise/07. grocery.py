def grocery_store(**kwargs):
    result = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    final = []
    for key, value in result.items():
        final.append(f'{key}: {value}')
    return '\n'.join(final)


print(grocery_store(bread=5, pasta=12, eggs=12,
                    ))
