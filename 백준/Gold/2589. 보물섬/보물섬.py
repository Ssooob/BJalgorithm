import sys
from collections import deque

# 최단거리라고 하는 거 보니까.. bfs를 써야할 듯..
# 두번 이상 지나가거나 = 방문처리, 멀리 돌아가서는 = 최단경로 BFS
# 모든 점에서부터 시작해서 최종 점까지 가는데, 그 중 최대거리를 구해라.. 
# 시간을 계속 저장하고 있다가, MAX로 산출하라는 의미? 

N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(input())

# 이동 방향 정의
dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]

def bfs(x,y):

    # 그럼 먼저 큐를 선언
    queue = deque()
    queue.append((x,y)) # 제일 첫번째 값을 queue에다가 넣음
    visited = [[0]*M for _ in range(N)]
    visited[x][y] = 1
    cnt = 0 

    # 엮여 있는 애들 넣어야하고, 종료 조건은 queue가 다 비었을 때까지
    while queue : # 큐가 빌 때까지
        x,y = queue.popleft() # 맨 밑에 있는 애를 뺌
        # 사방으로 확인 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 가장 상위 조건이 queue가 비는 것이고.. 그래프에 대한 조건이 밑으로 내려옴
            # 그래프 이외는 무시 

            if nx < 0 or ny < 0 or nx >= N or ny >= M  :
                continue

            # 그리고 해당 노드를 처음 밟았을 때만 해당
            elif graph[nx][ny] == 'L' and visited[nx][ny] == 0: # 최단거리로 숫자를 바꾸자
                visited[nx][ny] = visited[x][y] + 1 
                cnt = max(cnt,visited[nx][ny])
                queue.append((nx,ny))
    
    return cnt -1

result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            result = max(result,bfs(i,j)) 
print(result)