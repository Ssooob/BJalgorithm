n,c= map(int,input().split()) # n : 길이, c : 숫자는 모두 c보다 작거나 같다
numbers = list(map(int,input().split()))

res = []
nn = []
for i in range(len(numbers)):
    if len(res) == 0 :
        res.append([numbers[i],1,i])
        nn.append(numbers[i]) 
    else :
        if numbers[i] not in nn:
            res.append([numbers[i],1,i])
            nn.append(numbers[i])
        else :
            for j in range(len(res)) :
                if res[j][0] == numbers[i]:
                    res[j][1] += 1
res = sorted(res, key = lambda x : (-x[1],x[2]))
for k in range(len(res)):
    for kk in range(res[k][1]):
        print(res[k][0], end = ' ')