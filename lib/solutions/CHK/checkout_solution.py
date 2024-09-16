"""
Our price table and offers:
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+
"""
import math

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {"A": 50, "B": 30, "C": 20, "D": 15}
    illegal_input = False
    for letter in skus:
        if letter not in prices.keys():
            illegal_input = True
            total = -1
    if illegal_input == False:
        discounts = {"A": (3,130), "B": (2,45)}
        letter_dict = {char: skus.count(char) for char in set(skus)}
        totals = {}
        for key in letter_dict.keys():
            if key in discounts.keys():
                # for each key in letter_dict, do value % discounts value[0] and take that value away from total but add on value[1]
                discounts_applied = math.floor(letter_dict[key]/discounts[key][0])
                totals[key] = (letter_dict[key] - discounts_applied * discounts[key][0]) * prices[key] + discounts_applied*discounts[key][1]
            else:
                discounts_applied = 0
                totals[key] = letter_dict[key] * prices[key]
        total = 0
        for value in totals.values():
            total += value
    return total







