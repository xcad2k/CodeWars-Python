def Xbonacci(signature,n):
    length = len(signature)
    while len(signature) < n:
        signature.append(sum(signature[-length:]))
    return signature[:n]