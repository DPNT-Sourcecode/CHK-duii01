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
    discounts = {"AAA": 130, "BB": 45}
    sorted_skus = list(skus).sort()
    print(sorted_skus)


checkout("ACCDDABAC")

