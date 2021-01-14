def tribonacci(signature, n):
    while len(signature) != n:
        signature.append(signature[-1] + signature[-2] + signature[-3])
    return signature


print(tribonacci([0, 0, 1], 20))