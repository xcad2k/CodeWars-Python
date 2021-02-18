#####################################################################################
#                                                                                   #
#   NAME:     countNinesFromOneToN                                                  #
#   RANK:     5kyu                                                                  #
#   URL:      https://www.codewars.com/kata/55143152820d22cdf00001bb/train/python   #
#                                                                                   #
#####################################################################################
from time import time


def count_nines(n):
    return sum(map(lambda x: str(x).count("9"), range(9, n + 1)))


def count_nines2(n):
    return "".join(str(x) for x in range(9, n + 1) if "9" in str(x)).count("9")


def count_nines3(n):
    return "".join(x for x in map(lambda x: str(x), range(9, n + 1)) if "9" in x).count("9")


def count_nines4(n):
    return sum(str(x).count('9') for x in range(1, n))

def count_nines5(n):
    l = len(str(n))
    # for digit in str(n)[::-1]:
    #


start = time()
count_nines(10000000)
print(f"count_nines took  {time() - start}s")
start = time()
count_nines2(10000000)
print(f"count_nines2 took {time() - start}s")
start = time()
count_nines3(10000000)
print(f"count_nines3 took {time() - start}s")
start = time()
count_nines4(10000000)
print(f"count_nines4 took {time() - start}s")
start = time()
count_nines5(10000000)
print(f"count_nines5 took {time() - start}s")
