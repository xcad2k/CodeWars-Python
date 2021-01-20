import re

def get_order(order):
    menu_items = '(burger|fries|chicken|pizza|sandwich|onionrings|milkshake|coke)'
    
    return " ".join(map(lambda x: x.capitalize(), re.findall(menu_items, order)))

print(get_order(("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza")))