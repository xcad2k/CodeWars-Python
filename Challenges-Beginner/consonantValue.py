import re


def solve(s):
    return max(map(lambda x: sum(ord(a) - ord('a') + 1 for a in x), re.split('[aeiou]', s)))