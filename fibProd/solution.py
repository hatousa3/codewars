def productFib(prod):
    n1 = 0
    n2 = 1
    mul = 0
    while mul < prod:
        mul = (n1+n2)*n2
        n1, n2 = n2, n1+n2
    if mul == prod:
        return [n1, n2, True]
    return [n1, n2, False]
