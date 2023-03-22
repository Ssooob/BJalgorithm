n,k = map(int,input().split())
weights = list(map(int,input().split()))

def dfs(base):
    global cnt, weights

    if len(track) == n :
        # print(track)
        cnt += 1    
        return

    # 중복이 안되는 순서를 생성 
    for i in range(n):

        if visited[i] :
            continue

        next_base = base + weights[i] -k
        if next_base >= 500 : 
            visited[i] = True
            track.append(next_base)
            dfs(next_base)
            track.pop()
            visited[i] = False

visited = [False]*n
track,cnt = [],0
dfs(500)
print(cnt)