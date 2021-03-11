#####################################################################################
#                                                                                   #
#   NAME:     Domain name validator                                                 #
#   RANK:     5kyu                                                                  #
#   URL:      https://www.codewars.com/kata/5893933e1a88084be10001a3/train/python   #
#                                                                                   #
#####################################################################################

import re

def validate(domain):
    # Domain name must not be longer than 253 characters
    if(len(domain) > 253):
        return False

    # Domain name must contain at least one subdomain
    if("." not in domain):
        return False

    # Check for valid characters (A-z, 0-9, ., -)
    if(not re.match("^([A-Za-z0-9\.\-])*$", domain)):
        return False

    # Checks for levels (subdomains + domain + tdl)
    levels = domain.split(".")

    # Not more than 127 levels
    if(len(levels) > 127):
        return False

    # TLD must not be fully numerical
    if(levels[-1:][0].isnumeric()):
        return False

    for level in levels:
        # Level should not be empty
        if(level == ""):
            return False

        # Level names must not be longer than 63 characters
        if(len(level) > 63):
            return False

        # Level names must not start or end with - character
        if(level[-1:] == "-" or level[:1] == "-"):
            return False

    return True


print(validate('codewars'))
print(validate('g.co'))
print(validate('g!.co'))
