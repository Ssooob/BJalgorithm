T = int(input())
voca =[]
for t in range(T):
    voca.append(input())
voca = set(voca)
voca = list(voca)
voca.sort()
voca.sort(key = len)
print(*voca, sep='\n')