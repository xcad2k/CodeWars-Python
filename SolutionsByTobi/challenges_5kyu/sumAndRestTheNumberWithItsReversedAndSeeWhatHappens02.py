################################################################################
#                                                                              #
#   NAME:     Sum and Rest the Number with its Reversed and See What Happens   #
#   RANK:     5kyu                                                             #
#   URL:      https://www.codewars.com/kata/5603a9585480c94bd5000073           #
#                                                                              #
################################################################################

memo = []


def sum_dif_rev(n):
    i = memo[-1] if memo else 0
    while True:
        while len(memo) < n:
            i += 9
            r = int(str(i)[::-1])
            # i % 10 checks if the number ends with 0
            # r != i is necessary to not try % 0
            if i % 10 and r != i and (r + i) % abs(r - i) == 0:
                memo.append(i)
        return memo[n - 1]


print(sum_dif_rev(65))
