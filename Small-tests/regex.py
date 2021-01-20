import re

menu_items = '(burger|fries|chicken|pizza|sandwich|onionrings|milkshake|coke)'

string = "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"

print(re.findall(menu_items, string))

New-Cashier-Does-Not-Know-About-Space-or-Shift