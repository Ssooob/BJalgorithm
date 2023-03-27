import sys
sys.setrecursionlimit(10**7)


N,M,K = map(int,input().split())
graph = [[0]*M for _ in range(N)]

for _ in range(K):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1 


# 상하좌우에 대한 이동 값
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

size = 0 

def dfs(x,y):
    global size 

    # 종료 조건이 제일 위에 있어줘야함
    if x <= -1 or x >= N or y <=-1 or y >= M :
        return False
    
    # 방문 처리를 먼저 해주고..
    if graph[x][y] == 1 : # 쓰레기가 있다면  
        size += 1 # 쓰레기 크기 증가 
        graph[x][y] = 0 # 방문 처리 
        
        # 인접한 곳에 대한 탐색
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            
            dfs(nx,ny)

        return True # 근데 이제 1일때만 True인 것
    
    return False # 기본적으로 dfs를 수행할 때는 false

# 모든 노드에 대해 탐색
result = 0 
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True : # 만약 조건을 만족해서 True가 return되면, 
            result = max (result, size)
            size = 0 

print(result)