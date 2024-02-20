# def stock_availability(inventory, command, *args):
#     if command == 'delivery':
#         inventory.extend(args)
#     elif command == 'sell':
#         if args:
#             for data in args:
#                 if str(data).isdigit():
#                     inventory = inventory[data:]
#                 else:
#                     while data in inventory:
#                         inventory.remove(data)
#         else:
#             inventory = inventory[1:]
#     return inventory


class CandyShop:
    def __init__(self, inventory, command, *args):
        self.inventory = inventory
        self.command = command
        self.args = args

    def stock_availability(self):
        if self.command == 'delivery':
            self.inventory.extend(self.args)
        elif self.command == 'sell':
            if self.args:
                for data in self.args:
                    if str(data).isdigit():
                        self.inventory = self.inventory[data:]
                    else:
                        while data in self.args:
                            self.inventory.remove(data)
            else:
                self.inventory = self.inventory[1:]

        return self.inventory


def stock_availability(*args):
    output = CandyShop(*args).stock_availability()
    return output


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
