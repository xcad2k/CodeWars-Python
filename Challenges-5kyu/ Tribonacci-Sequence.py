def tribonacci(signature, n):

    for i in range(n):
        signature.append(
            signature[i] +
            signature[i + 1] +
            signature[i + 2]
        )

    return signature[:n]


print(tribonacci([0, 0, 1], 10))
