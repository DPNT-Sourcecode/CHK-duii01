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
    if illegal_input == False:
        discounts = {"A": (3,130), "B": (2,45)}
        get_free = {"E": (2,(1,"B"))}
        letter_dict = {char: skus.count(char) for char in set(skus)}
        for key in get_free.keys():
            # if letter is in letter_dict then lower divide value by value in dict. Multiply that with number in value multiply by price of B and that is discount
            if key in letter_dict.keys():
                free_discount_applied = math.floor(letter_dict[key]/get_free[key][0])
                reduction = free_discount_applied * get_free[key][1][0] * prices[get_free[key][1][1]]
                print(reduction)
        totals = {}
        for key in letter_dict.keys():
            if key in discounts.keys():
                # for each key in letter_dict, do value % discounts value[0] and take that value away from total but add on value[1]
                discounts_applied = math.floor(letter_dict[key]/discounts[key][0])
                totals[key] = (letter_dict[key] - discounts_applied * discounts[key][0]) * prices[key] + discounts_applied*discounts[key][1]
            else:
                totals[key] = letter_dict[key] * prices[key]
        total = 0
        for value in totals.values():
            total += value
    return total


checkout("EE")
checkout("EEE")
checkout("EEEE")





