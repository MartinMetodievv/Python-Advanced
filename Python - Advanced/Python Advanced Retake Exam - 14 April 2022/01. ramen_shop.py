# from _collections import deque
#
# bowls_of_ramen = [int(x) for x in input().split(', ')]
# customers = deque([int(x) for x in input().split(', ')])
#
# while bowls_of_ramen and customers:
#     cur_bowl = bowls_of_ramen.pop()
#     cur_customer = customers.popleft()
#
#     if cur_bowl == cur_customer:
#         continue
#     if cur_bowl > cur_customer:
#         cur_bowl -= cur_customer
#         bowls_of_ramen.append(cur_bowl)
#     elif cur_bowl < cur_customer:
#         cur_customer -= cur_bowl
#         customers.appendleft(cur_customer)
# if not customers:
#     print("Great job! You served all the customers.")
#     if bowls_of_ramen:
#         print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_of_ramen)}")
# else:
#     print("Out of ramen! You didn't manage to serve all customers.")
#     print(f"Customers left: {', '.join(str(x) for x in customers)}")
from _collections import deque


class RamenShop:
    def __init__(self, bowls, customers):
        self.bowls = bowls
        self.customers = deque(customers)
        self.log = []

    def feed_clients(self):
        while self.bowls and self.customers:
            cur_bowl = self.bowls.pop()
            cur_customer = self.customers.popleft()

            if cur_bowl == cur_customer:
                continue
            if cur_bowl > cur_customer:
                cur_bowl -= cur_customer
                self.bowls.append(cur_bowl)
            elif cur_bowl < cur_customer:
                cur_customer -= cur_bowl
                self.customers.appendleft(cur_customer)

    def __repr__(self):
        if not self.customers:
            self.log.append("Great job! You served all the customers.")
            if self.bowls:
                self.log.append(f"Bowls of ramen left: {', '.join(str(x) for x in self.bowls)}")
        else:
            self.log.append("Out of ramen! You didn't manage to serve all customers.")
            self.log.append(f"Customers left: {', '.join(str(x) for x in self.customers)}")
        return '\n'.join(self.log)


bowls_of_ramen = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])

output = RamenShop(bowls_of_ramen, customers)
output.feed_clients()
print(output)
