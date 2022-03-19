def array_diff(a, b):
    #your code here
    lis = []
    for i in a:
        if i not in b:
            lis.append(i)
    return lis
