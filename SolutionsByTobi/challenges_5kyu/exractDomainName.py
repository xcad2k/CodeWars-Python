#####################################################################################
#                                                                                   #
#   NAME:     Extract the domain name from a URL                                    #
#   RANK:     5kyu                                                                  #
#   URL:      https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python   #
#                                                                                   #
#####################################################################################

import re


# pretty special use case... not working with subdomains (except www)
def domain_name(url):
    return re.sub("(https?://)?(www\.)?", "", url).split(".")[0]


print(domain_name("https://123.net"))
