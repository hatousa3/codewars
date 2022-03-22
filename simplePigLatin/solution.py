def pig_it(text):
    lis = []
    for x in text.split(' '):
        if x == '!' or x == '?':
            lis.append(x)
        else:
            lis.append(x[1:] + x[0] + 'ay')
            
    return ' '.join(lis)
