def shopping_cart(*products):
    limits = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2,
    }

    shopping_list = {
        "Soup": [],
        "Pizza": [],
        "Dessert": [],
    }
    final_result = ""

    for item in products:
        if item == "Stop":
            break
        else:
            meal, product = item

        if (len(shopping_list[meal]) < limits[meal]) and (product not in shopping_list[meal]):
            shopping_list[meal].append(product)

    shopping_list = dict(sorted(shopping_list.items(), key=lambda x: (-len(x[1]), x[0])))

    for meal, products in shopping_list.items():
        final_result += f"{meal}:\n"
        if products:
            for item in sorted(products):
                final_result += f" - {item}\n"

    if not shopping_list["Soup"] and not shopping_list["Pizza"] and not shopping_list["Dessert"]:
        return "No products in the cart!"
    return final_result
#
#
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))
#
# # print(shopping_cart(
# #     ('Pizza', 'ham'),
# #     ('Dessert', 'milk'),
# #     ('Pizza', 'ham'),
# #     'Stop',
# # ))
#
# # print(shopping_cart(
# #     'Stop',
# #     ('Pizza', 'ham'),
# #     ('Pizza', 'mushrooms'),
# # ))
