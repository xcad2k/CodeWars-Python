#####################################################################################
#                                                                                   #
#   NAME:     Mixbonacci                                                            #
#   RANK:     5kyu                                                                  #
#   URL:      https://www.codewars.com/kata/5811aef3acdf4dab5e000251/train/python   #
#                                                                                   #
#####################################################################################

def mixbonacci(pattern, length):
    res = []
    if len(pattern) == 0:
        return res
    fib = fibonacci()
    pad = padovan()
    pel = pell()
    jac = jacobsthal()
    tri = tribonacci()
    tet = tetranacci()
    for i in range(length):
        current_pattern = pattern[i % len(pattern)]
        if current_pattern == 'fib':
            res.append(next(fib))
        elif current_pattern == 'pad':
            res.append(next(pad))
        elif current_pattern == 'pel':
            res.append(next(pel))
        elif current_pattern == 'jac':
            res.append(next(jac))
        elif current_pattern == 'tri':
            res.append(next(tri))
        elif current_pattern == 'tet':
            res.append(next(tet))
    return res


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def tribonacci():
    a, b, c = 0, 0, 1
    yield a
    yield b
    while True:
        yield c
        a, b, c = b, c, a + b + c


def tetranacci():
    a, b, c, d = 0, 0, 0, 1
    yield a
    yield b
    yield c
    while True:
        yield d
        a, b, c, d = b, c, d, a + b + c + d


def padovan():
    a, b, c = 1, 0, 0
    yield a
    yield b
    while True:
        yield c
        a, b, c = b, c, a + b


def pell():
    a, b = 0, 1
    yield a
    while True:
        yield b
        a, b = b, 2 * b + a


def jacobsthal():
    a, b = 0, 1
    yield a
    while True:
        yield b
        a, b = b, 2 * a + b


print(mixbonacci(["pad"], 20))
