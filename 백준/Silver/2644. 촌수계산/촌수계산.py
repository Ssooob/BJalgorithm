import sys
sys.setrecursionlimit(300000)

n = int(input())
a,b = map(int,input().split())
m = int(input())
graph = [[]for _ in range(n+1)]
visited = [False]*(n+1)
cnt = [0]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    #  서로서로 연결되어야하기 때문에
    graph[x].append(y)
    graph[y].append(x)

flag = False
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            cnt[i] = cnt[v] + 1
            dfs(i)
dfs(a)
if cnt[b]>0:
    print(cnt[b])
else :
    print(-1)