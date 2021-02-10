#####################################################################################
#                                                                                   #
#   NAME:     Pete, the Baker                                                       #
#   RANK:     5kyu                                                                  #
#   URL:      https://www.codewars.com/kata/525c65e51bf619685c000059/train/python   #
#                                                                                   #
#####################################################################################

def cakes(recipe, available):
    return min(available.get(ingredient, 0) // recipe[ingredient] for ingredient in recipe)
