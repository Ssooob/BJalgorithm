N, M = map(int, input().split())
li = list(map(int, input().split()))
s, e = 0, max(li)*M
res = 0
while s <= e:
    m = (s+e)//2
    if sum([m//n for n in li]) >= M:
        res = m
        e = m-1
    else:
        s = m+1
print(res)