def dfs(level):
    if level == m:
        print(' '.join(map(str,result)))
        return
    for i in range(1, n+1):
        if visited[i] == True:
            continue

        result[level] = i
        visited[i] = True
        dfs(level + 1)
        visited[i] = False

n,m = map(int,input().split())
visited = [False]*(n+1)
result = [0] * m
dfs(0)