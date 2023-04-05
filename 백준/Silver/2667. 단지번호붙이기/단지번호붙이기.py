n = int(input())
graph = [list(map(int,input())) for _ in range(n)]

# 방향 설정
dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[False]*n for _ in range(n)]
group = [0]# [0]*(n**2)
def dfs(x,y,g):
    if x < 0 or x >= n or y < 0 or y >=n :
        return False

    if (visited[x][y] == False) and (graph[x][y] == 1):
        visited[x][y] = True
        group[g] += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny,g)
        return True
    return False

cnt = 0
g = 0
for i in range(n):
    for j in range(n):
        if dfs(i,j,g) :
            cnt += 1
            group.append(0)
            g += 1

print(cnt)
print(*sorted(group)[1:], sep ='\n')