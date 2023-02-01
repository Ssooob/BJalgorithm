contry,score = map(int,input().split())
rank = []
for c in range(contry) :
    rank.append(list(map(int,input().split())))
sorted_rank = sorted(rank,key = lambda x : (-x[1],-x[2],-x[3]))
for i in range(contry):
    if sorted_rank[i][0] == score:
        index = i
for i in range(contry):
    if sorted_rank[index][1:] == sorted_rank[i][1:]:
        print(i+1)
        break
