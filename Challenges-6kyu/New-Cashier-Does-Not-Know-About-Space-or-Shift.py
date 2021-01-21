import re


def get_order(order):
    # init a regex string for all menu items
    menu_items = '(burger|fries|chicken|pizza|sandwich|onionrings|milkshake|coke)'

    # returns concatenated string of all menu items in the right order
    return " ".join(
        # sort strings based on "lambda str" function
        sorted(
            # capitalizes all menu items that a re found in the order
            map(
                lambda x: x.capitalize(), re.findall(menu_items, order)
            ),

            # returns the position of the equivalent menu item
            key=lambda str: menu_items.index(str.lower())
        )
    )

print(get_order(("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza")))
