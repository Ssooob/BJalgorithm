n = int(input())
s,g,p,d = map(int,input().split())
rank = list(input())

prev = 0
money = 0
for r in range(len(rank)):
    if rank[r] == 'B':
        money += s-1 - prev 
        prev = s-1-prev 
    elif rank[r] == 'S':
        money += g-1-prev 
        prev = g-1-prev 
    elif rank[r] == 'G':
        money += p-1-prev 
        prev = p-1-prev 
    elif rank[r] == 'P':
        money += d-1-prev 
        prev= d-1-prev 
    elif rank[r] == 'D':
        money += d

print(money)