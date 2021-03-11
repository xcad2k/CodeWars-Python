#####################################################################################
#                                                                                   #
#   NAME:     Domain name validator                                                 #
#   RANK:     5kyu                                                                  #
#   URL:      https://www.codewars.com/kata/5893933e1a88084be10001a3/train/python   #
#                                                                                   #
#####################################################################################
import re


def validate(domain: str):
    return len(domain) < 254 and bool(re.match(r'^(([a-zA-Z\d][a-zA-Z\d-]{0,61}[a-zA-Z\d]|[a-zA-Z\d])\.){1,127}(?!-)[a-z0-9-]*[a-z-][a-z0-9-]*(?<!-)$', domain, re.IGNORECASE))
