def shop_from_grocery_list(budget, grocery=list, *args):
    buy = []
    for item, price in args:
        if item not in buy:
            if item in grocery:
                if budget >= price:
                    buy.append(item)
                    budget -= price
                elif budget < price:
                    break
            else:
                continue
        else:
            continue
    if len(grocery) == len(buy):
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        new = []
        for x in grocery:
            if x not in buy:
                new.append(x)
        return f"You did not buy all the products. Missing products: {', '.join(new)}."

# print(shop_from_grocery_list(100, ["tomato", "cola"], ("cola", 5.8), ("tomato", 10.0), ("tomato", 20.45), ))
# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))
# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat", "chocolate"],
#     ("cola", 15.8),
#     ("chocolate", 30),
#     ("tomato", 15.85),
#     ("chips", 50),
#     ("meat", 22.99),
# ))
