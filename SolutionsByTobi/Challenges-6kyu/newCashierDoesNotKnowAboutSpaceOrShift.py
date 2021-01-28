"""
CODEWARS-CHALLENGE: New Cashier Does Not Know About Space or Shift
URL: https://www.codewars.com/kata/5d23d89906f92a00267bb83d
"""


import re


def get_order(order):
    lookup = ["burger", "fries", "chicken", "pizza", "sandwich", "onionrings", "milkshake", "coke"]
    return " ".join(sorted(map(lambda x: x.capitalize(), re.findall('|'.join(lookup), order)), key=lambda x: lookup.index(x.lower())))


print(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"))
