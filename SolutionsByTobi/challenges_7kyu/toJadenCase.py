#####################################################################################
#                                                                                   #
#   NAME:     Jaden Casing Strings                                                  #
#   RANK:     7kyu                                                                  #
#   URL:      https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python   #
#                                                                                   #
#####################################################################################

def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split(" "))


print(to_jaden_case("This is a test"))
