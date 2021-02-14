#####################################################################################
#                                                                                   #
#   NAME:     Snail                                                                 #
#   RANK:     4kyu                                                                  #
#   URL:      https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python   #
#                                                                                   #
#####################################################################################

def snail(snail_map, direction=0):
    current = []
    if len(snail_map) == 0:
        return []
    if direction == 0:
        current = snail_map[0]
        snail_map = snail_map[1:]
    if direction == 1:
        current = [x[-1] for x in snail_map]
        snail_map = [x[:-1] for x in snail_map]
    if direction == 2:
        current = snail_map[-1][::-1]
        snail_map = snail_map[:-1]
    if direction == 3:
        current = [x[0] for x in snail_map][::-1]
        snail_map = [x[1:] for x in snail_map]

    direction += 1
    direction %= 4
    return [*current, *snail(snail_map, direction)]


array = [[1,  2,  3,  4,  5],
         [6,  7,  8,  9,  10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25]]
print(snail(array))
