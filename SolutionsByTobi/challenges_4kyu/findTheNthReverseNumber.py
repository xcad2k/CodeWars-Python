#####################################################################################
#                                                                                   #
#   NAME:     Find the nth Reverse Number                                           #
#   RANK:     4kyu                                                                  #
#   URL:      https://www.codewars.com/kata/600c18ec9f033b0008d55eec/train/python   #
#                                                                                   #
#####################################################################################

def find_reverse_number(n):
    count = 0
    index = -1
    while True:
        index += 1
        if str(index) == str(index)[::-1]:
            count += 1
        if count == n:
            return index


print(find_reverse_number(100000000000))
