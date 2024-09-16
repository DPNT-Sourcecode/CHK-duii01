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

        for key in get_free.keys():
            if key in letter_dict.keys():
                free_discount_applied = math.floor(letter_dict[key]/get_free[key][0])
                reduction = free_discount_applied * get_free[key][1][0]
                if get_free[key][1][1] in letter_dict.keys():
                    letter_dict[get_free[key][1][1]] -= reduction
        totals = {}

        discounts = {"A": [(5, 120), (3, 130)], "B": [(2, 45)]}
        for key in letter_dict.keys():
            if letter_dict[key] < 0:
                pass
            elif key in discounts.keys():
                for deal in discounts[key]:
                    discounts_applied = math.floor(letter_dict[key]/deal[0])
                    totals[key] = (letter_dict[key] - discounts_applied * discounts[key][0]) * prices[key] + discounts_applied*discounts[key][1]
            else:
                totals[key] = letter_dict[key] * prices[key]
        total = sum(totals.values())
    return total


dict1 = {"a": 1, "b": 2}
for i in dict1:
    print(i)


# class CheckoutSystem:
#     def __init__(self):
#         self.prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
#         self.discounts = {"A": (3, 130), "B": (2, 45)}
#         self.get_free = {"E": (2, (1, "B"))}
#
#
#     def checkout(self, skus):
#         illegal_input = False
#         for letter in skus:
#             if letter not in self.prices.keys():
#                 illegal_input = True
#                 total = -1
#                 break
#
#         if not illegal_input:
#             letter_dict = {char: skus.count(char) for char in set(skus)}
#             for key in self.get_free.keys():
#                 free_discount_applied = math.floor(letter_dict[key]/self.get_free[key][0])
#                 reduction = free_discount_applied * self.get_free[key][1][0]
#                 if self.get_free[key][1][1] in letter_dict.keys():
#                     letter_dict[self.get_free[key][1][1]] -= reduction
#
#         totals = {}
#         for key in letter_dict.keys():
#             if letter_dict[key] < 0:
#                 pass
#             elif key in self.discounts.keys():
#                 discounts_applied = math.floor(letter_dict[key] / self.discounts[key][0])
#                 totals[key] = (letter_dict[key] - discounts_applied * self.discounts[key][0]) * self.prices[key] + discounts_applied * self.discounts[key][1]
#             else:
#                 totals[key] = letter_dict[key] * self.prices[key]
#
#         total = sum(totals.values())
#         return total
#
# checkout_system = CheckoutSystem()
# total_price = checkout_system.checkout("ABCD")
# print(total_price)