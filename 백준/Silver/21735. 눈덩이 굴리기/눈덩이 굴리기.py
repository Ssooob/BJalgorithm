import sys
input = sys.stdin.readline
N,M = map(int,input().split())
snows = [0] + list(map(int,input().split()))
res = -1 
def dfs(idx, snow, time):
    global res
    if time < 0 :
        return
    res = max(res,snow)
    if idx +1 <= N :
        dfs(idx+1,snow+snows[idx+1],time-1)
    if idx +2 <= N :
        dfs(idx+2,snow//2+snows[idx+2],time-1)
dfs(0,1,M)
print(res)