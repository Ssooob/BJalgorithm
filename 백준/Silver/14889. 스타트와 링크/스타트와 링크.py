N = int(input())
effort = [list(map(int,input().split()))for _ in range(N)]
min_diff = 1e9
s,l = [],[]

def dfs(depth, idx): # idx가 
    global min_diff
    # depth 기준 기반 팀 나누기   
    if depth == N//2:
        s_effort,l_effort = 0,0
        # print(visited)
        
        # 능력치 구하기
        for i in range(N-1):
            for j in range(i+1,N):
                if visited[i] == True and visited[j] == True:
                    #print('stark',j,k)
                    s_effort += effort[i][j]
                    s_effort += effort[j][i]
                elif visited[i] == False and visited[j] == False:
                    #print('link',j,k)
                    l_effort += effort[i][j]
                    l_effort += effort[j][i]
        #print(s_effort,l_effort,min_diff)
        # 최소치 구하기 
        min_diff = min(min_diff,abs(s_effort-l_effort))

    # 중복 없는 수열을 구하기 위함  
    for i in range(idx, N): # 그냥 1~N까지 돌면, 
        if visited[i]:
            continue
        visited[i] = True
        dfs(depth+1, i+1)
        visited[i] = False
        
visited = [False]*(N)
dfs(0,0)
print(min_diff)