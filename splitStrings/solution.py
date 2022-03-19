def solution(s):
    lis=[]
    for i in range(len(s)):
        if i%2 == 0 and i < len(s)-1:
            lis.append(s[i:i+2])
        if i%2 == 0 and i == len(s)-1:
            lis.append(s[len(s)-1]+'_')
            
    return lis
