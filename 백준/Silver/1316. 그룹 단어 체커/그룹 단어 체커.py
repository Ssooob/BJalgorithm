T = int(input())
cnt = 0
for t in range(T):
    voca = input()
    alp = [0]*26 
    break_point = False
    for v in range(len(voca)) :
        if alp[ord(voca[v])-ord('a')] == 0 :
            alp[ord(voca[v])-ord('a')] += 1
            continue
        elif alp[ord(voca[v])-ord('a')] != 0 and voca[v-1] == voca[v] :
            continue
        elif  alp[ord(voca[v])-ord('a')] != 0 and voca[v-1] != voca[v] :
            break_point = True
            break
    if break_point == False :
        cnt += 1
print(cnt)