#####################################################################################
#                                                                                   #
#   NAME:     Highest Rank Number in an Array                                       #
#   RANK:     6kyu                                                                  #
#   URL:      https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/train/python   #
#                                                                                   #
#####################################################################################

def highest_rank(arr):
    num_occurrences = {}

    for number in arr:
        if num_occurrences.get(number):
            num_occurrences[number] += 1
        else:
            num_occurrences[number] = 1

    highest_number = 0
    counter = 0

    for num, occurrences in num_occurrences.items():
        if occurrences == counter:
            if num > highest_number:
                highest_number = num
                counter = occurrences
        elif occurrences > counter:
            highest_number = num
            counter = occurrences

    return highest_number


print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]))
