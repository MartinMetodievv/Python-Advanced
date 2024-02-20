def shopping_cart(*args):
    meals = {
        'Pizza': [],
        'Soup': [],
        'Dessert': []
    }
    limits = {
        'Pizza': 4,
        'Soup': 3,
        'Dessert': 2
    }
    message = ''
    for info in args:
        if info == 'Stop':
            break
        else:
            meal, product = info

        if (len(meals[meal]) < limits[meal]) and (product not in meals[meal]):
            meals[meal].append(product)

    meals = dict(sorted(meals.items(), key=lambda x: (-len(x[1]), x[0])))
    for k, v in meals.items():
        message += f'{k}:\n'
        if v:
            for x in sorted(v):
                message += f'- {x}\n'
    if not meals['Soup'] and not meals['Pizza'] and not meals['Dessert']:
        return "No products in the cart!"
    return message
