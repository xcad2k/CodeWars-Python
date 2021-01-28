"""
CODEWARS-CHALLENGE: Jaden Casing Strings
URL: https://www.codewars.com/kata/5390bac347d09b7da40006f6
"""

import re


def to_jaden_case(string):
    # this replaces using regex
    # I select every combination of a space and a char
    # and replaces it using groups
    # since I select this as a group I can put the group back in (with an to upper so that this char is beeing capitalized)

    # A lambda function is simply a function that can be written inline and that is anonymous

    return re.sub(pattern="( .)", repl=lambda pat: pat.group(1).upper(), string=string)


print(to_jaden_case("This is a test using regex replace"))
