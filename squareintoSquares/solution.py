def decompose(n):
    # your code
    lis = []
    sq = n**2
    for x in range(n-1,0,-1):
        if sq >= (x)**2:
            lis.append(x)
            sq -= (x)**2

    if sq == 0:
        return lis[::-1]
    else:
        return None
        
