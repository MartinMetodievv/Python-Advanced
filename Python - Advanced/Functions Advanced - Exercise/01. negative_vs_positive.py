def sum_nums(*args):
    pos_sum = 0
    neg_sum = 0
    for el in args:
        if el > 0:
            pos_sum += el
        else:
            neg_sum += el
    # pos_sum = sum([int(x) for x in args if x > 0])
    # neg_sum = sum([int(x) for x in args if x < 0])
    # neg_sum = sum(list(filter(lambda x: x < 0, args)))
    return neg_sum, pos_sum


num = [int(x) for x in input().split()]
print(sum_nums(*num)[0])
print(sum_nums(*num)[1])
if abs(sum_nums(*num)[0]) > sum_nums(*num)[1]:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
