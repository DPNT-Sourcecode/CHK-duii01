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
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
+------+-------+------------------------+
"""
import math
import csv
import pandas as pd

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10, }
    with open('C:\\Users\\dgcje\\OneDrive - School of Automation\\Documents\\runner-for-python-windows\\accelerate_runner\\prices.csv', "r", ) as prices_file:
        csv_reader = csv.reader(prices_file, delimiter='|')
        prices = {rows[0].strip(): int(rows[1].strip()) for rows in csv_reader}
    illegal_input = False
    for letter in skus:
        if letter not in prices.keys():
            illegal_input = True
            total = -1
            break
    if illegal_input == False:
        get_free = {
            "E": (2, (1, "B")),
            "F": (3, (1, "F")),
            "N": (3, (1, "M")),
            "R": (3, (1, "Q")),
            "U": (4, (1, "U"))
        }
        letter_count = {char: skus.count(char) for char in set(skus)}

        for key in get_free:
            if key in letter_count:
                free_discount_applied = math.floor(letter_count[key]/get_free[key][0])
                reduction = free_discount_applied * get_free[key][1][0]
                if get_free[key][1][1] in letter_count.keys():
                    letter_count[get_free[key][1][1]] -= reduction
        totals = {key: 0 for key in prices}

        discounts = {
            "A": [(5, 200), (3, 130)],
            "B": [(2, 45)],
            "H": [(10, 80), (5, 40)],
            "K": [(2, 150)],
            "P": [(5, 200)],
            "Q": [(3, 80)],
            "V": [(3, 130), (2, 90)]
        }
        for key in letter_count:
            if letter_count[key] < 0:
                pass
            elif key in discounts:
                for deal in discounts[key]:
                    discounts_applied = math.floor(letter_count[key]/deal[0])
                    letter_count[key] = letter_count[key] - discounts_applied * deal[0]
                    totals[key] += discounts_applied*deal[1]
                totals[key] += letter_count[key] * prices[key]
            else:
                totals[key] = letter_count[key] * prices[key]
        total = sum(totals.values())
    return total

