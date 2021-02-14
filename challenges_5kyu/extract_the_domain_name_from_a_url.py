#####################################################################################
#                                                                                   #
#   NAME:     Extract the domain name from a URL                                    #
#   RANK:     5kyu                                                                  #
#   URL:      https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python   #
#                                                                                   #
#####################################################################################

import re


def domain_name(url):
    return re.sub("(.*//)|www.", "", url).split(".")[0]


print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))
