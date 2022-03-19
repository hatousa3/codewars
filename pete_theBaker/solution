def cakes(recipe, available):
    lis=[]
    for i in recipe:
        if i in available:
            lis.append(int(available[i]/recipe[i]))
        else:
            return 0
    return min(lis)
