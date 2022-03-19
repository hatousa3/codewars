def tribonacci(signature, n):
    #your code here
    lis = signature[:n]
    for i in range(n-3):
        lis.append(sum(lis[-3:]))
    return lis
