string = list(input())
alpha = [-1]*26
idx = 0
for s in string :
    if alpha[ord(s)-ord('a')] != -1 :
        idx +=1
        pass
    else :
        alpha[ord(s)-ord('a')] = idx
        idx +=1
print(*alpha)