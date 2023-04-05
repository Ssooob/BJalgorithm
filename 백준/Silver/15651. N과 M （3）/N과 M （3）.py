def dfs2(level):
    if level == m:
        print(' '.join(map(str, result)))
        return
    for i in range(1,n+1):
        result[level] = i
        dfs2(level + 1)
n,m = map(int,input().split())
result = [0] * m
dfs2(0)