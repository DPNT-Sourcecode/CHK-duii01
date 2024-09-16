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

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {"A": 50, "B": 30, "C": 20, "D": 15}
    discounts = {"A": (3,130), "B": (2,45)}
    letter_dict = {char: skus.count(char) for char in set(skus)}
    totals = {}
    print(letter_dict)
    for key in letter_dict.keys():
        print(key)
        # for each key in letter_dict, do value % discounts value[0] and take that value away from total but add on value[1]
        discounts_applied = letter_dict[key]%discounts[key][0]
        print(discounts_applied)
        totals[key] = (letter_dict[key]-discounts_applied*discounts[key][0])*prices[key]+discounts_applied[1]
    print(totals)

checkout("AAABCCCCCDD")





