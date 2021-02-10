#####################################################################################
#                                                                                   #
#   NAME:     Mixbonacci                                                            #
#   RANK:     5kyu                                                                  #
#   URL:      https://www.codewars.com/kata/5811aef3acdf4dab5e000251/train/python   #
#                                                                                   #
#####################################################################################

def mixbonacci(pattern, length):

    if pattern == [] or length == 0:
        return []

    outputdict = {}
    outputlist = []
    counter = {}

    for p in pattern:
        if p == "fib":
            fibList = [0, 1]
            for i in range(length + len(pattern)):
                fibList.append(
                    fibList[i] + fibList[i + 1]
                )
            outputdict["fib"] = fibList
            counter["fib"] = 0

        if p == "pad":
            padList = [1, 0, 0]
            for i in range(length + len(pattern)):
                padList.append(
                    padList[i] + padList[i + 1]
                )
            outputdict["pad"] = padList
            counter["pad"] = 0

        if p == "jac":
            jacList = [0, 1]
            for i in range(length + len(pattern)):
                jacList.append(
                    (jacList[i] * 2) + jacList[i + 1]
                )
            outputdict["jac"] = jacList
            counter["jac"] = 0

        if p == "pel":
            pelList = [0, 1]
            for i in range(length + len(pattern)):
                pelList.append(
                    pelList[i] + (pelList[i + 1] * 2)
                )
            outputdict["pel"] = pelList
            counter["pel"] = 0

        if p == "tri":
            triList = [0, 0, 1]
            for i in range(length + len(pattern)):
                triList.append(
                    triList[i] + triList[i + 1] + triList[i + 2]
                )
            outputdict["tri"] = triList
            counter["tri"] = 0

        if p == "tet":
            tetList = [0, 0, 0, 1]
            for i in range(length + len(pattern)):
                tetList.append(
                    tetList[i] + tetList[i + 1] + tetList[i + 2] + tetList[i + 3]
                )
            outputdict["tet"] = tetList
            counter["tet"] = 0

    i = 0
    while i < length:
        for p in pattern:
            outputlist.append(outputdict[p][counter[p]])
            counter[p] += 1
            i += 1

    return outputlist[:length]


print(mixbonacci(['jac', 'tet', 'jac', 'pad', 'jac', 'fib', 'pad', 'tet', 'jac', 'pad', 'pel', 'pel', 'pel'], 1))
