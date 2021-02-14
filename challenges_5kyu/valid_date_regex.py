#####################################################################################
#                                                                                   #
#   NAME:     validDate Regex                                                       #
#   RANK:     5kyu                                                                  #
#   URL:      https://www.codewars.com/kata/548db0bd1df5bbf29b0000b7/train/python   #
#                                                                                   #
#####################################################################################

# TODO: CHALLENGE IS NOT FINISHED!!!

import re


def valid_date(string):
    date = re.findall('\[\d{2}\-\\d{2}]', string)
    numbers = re.findall('\d{2}', date[0])

    return numbers


print(valid_date('ignored [08-11] ignored'))
