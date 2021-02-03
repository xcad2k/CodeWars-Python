#####################################################################################
#                                                                                   #
#   NAME:     Break camelCase                                                       #
#   RANK:     6kyu                                                                  #
#   URL:      https://www.codewars.com/kata/5208f99aee097e6552000148/train/python   #
#                                                                                   #
#####################################################################################

# Solution 1
def solution(s):
    return "".join(" " + char if char.isupper() else char for char in s)


# Tests
print(solution("helloWorld"))
print(solution("breakCamelCase"))
