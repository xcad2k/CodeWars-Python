def xbonacci(signature, n):

    numElements = len(signature)

    for i in range(n):
        signature.append(
            sum(signature[-numElements:])
        )

    return signature[:n]


print(xbonacci([0, 0, 1, 1], 10))
