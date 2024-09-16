"""
Our price table and offers:
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+
"""
import math

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
    illegal_input = False
    for letter in skus:
        if letter not in prices.keys():
            illegal_input = True
            total = -1
            break
    if illegal_input == False:
        get_free = {"E": (2, (1, "B"))}
        letter_dict = {char: skus.count(char) for char in set(skus)}

        for key in get_free:
            if key in letter_dict:
                free_discount_applied = math.floor(letter_dict[key]/get_free[key][0])
                reduction = free_discount_applied * get_free[key][1][0]
                if get_free[key][1][1] in letter_dict.keys():
                    letter_dict[get_free[key][1][1]] -= reduction
        totals = {}

        discounts = {"A": [(5, 120), (3, 130)], "B": [(2, 45)]}
        for key in letter_dict:
            if letter_dict[key] < 0:
                pass
            elif key in discounts:
                for deal in discounts[key]:
                    discounts_applied = math.floor(letter_dict[key]/deal[0])
                    totals[key] += (letter_dict[key] - discounts_applied * deal[0]) * prices[key] + discounts_applied*deal[1]
                    letter_dict[key] -= discounts_applied * deal[0]
            else:
                totals[key] = letter_dict[key] * prices[key]
        total = sum(totals.values())
    return total


print(checkout("AAAAABAAA"))