def cakes(recipe, available):
    return min(available.get(ingredient, 0) // recipe[ingredient] for ingredient in recipe)
