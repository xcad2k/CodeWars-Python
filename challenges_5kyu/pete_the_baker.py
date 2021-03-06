#####################################################################################
#                                                                                   #
#   NAME:     Pete, the Baker                                                       #
#   RANK:     5kyu                                                                  #
#   URL:      https://www.codewars.com/kata/525c65e51bf619685c000059/train/python   #
#                                                                                   #
#####################################################################################

def cakes(recipe, available):
    return min([available.get(object) // recipe.get(object) for object in recipe])


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))
