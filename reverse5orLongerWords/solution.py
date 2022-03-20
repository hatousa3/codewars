def spin_words(sentence):
    lis=[]
    s = ""
    for word in sentence.split(' '):
        if len(word) >= 5:
            lis.append(word[::-1])
        else:
            lis.append(word)
    return ' '.join(lis)
        
        
