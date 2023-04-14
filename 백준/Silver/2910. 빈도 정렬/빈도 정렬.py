n,c= map(int,input().split()) # n : 길이, c : 숫자는 모두 c보다 작거나 같다
numbers = list(map(int,input().split()))
res = {}
idx = 0 
for i in numbers:
    if i not in res:
        res[i] = [1, idx] 
        idx += 1
    else :
        res[i][0] += 1
res = sorted(res.items(), key = lambda x : (-x[1][0],x[1][1]))
for r in res :
    for rr in range(r[1][0]):
        print(r[0], end = ' ')