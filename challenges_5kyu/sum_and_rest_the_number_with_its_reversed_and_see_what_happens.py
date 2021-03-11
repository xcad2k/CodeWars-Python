################################################################################
#                                                                              #
#   NAME:     Sum and Rest the Number with its Reversed and See What Happens   #
#   RANK:     5kyu                                                             #
#   URL:      https://www.codewars.com/kata/5603a9585480c94bd5000073           #
#                                                                              #
################################################################################


def reverse_number(n):
    return int(str(n)[::-1])


def sum_dif_rev(n):
    numbers = []
    index_reached = False
    current_number = 36

    while not index_reached:
        current_number += 9

        if str(current_number)[-1:] == "0":
            continue

        reversed_number = reverse_number(current_number)

        if reversed_number == current_number:
            continue

        if (current_number + reversed_number) % abs(current_number - reversed_number) == 0:
            # print(f"{current_number} added")
            numbers.append(current_number)

            if n == len(numbers):
                # print("Last Number found")
                return current_number
                break

print(sum_dif_rev(65))
