
n = int(input())
tmp = ''
res = []
for i in range(n):
    l = list(input())
    for j in range(len(l)):
        if l[j].isdigit(): # 숫자라면
            tmp+=l[j]
        else :
            if tmp != '':
                tmp.replace 
                res.append(tmp)
                tmp = ''
    if tmp != '':
        res.append(tmp)
        tmp = ''
    tmp = ''

res = list(map(int,res))
print(*sorted(res),sep = '\n' ) 