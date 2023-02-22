import sys
from collections import deque
input=sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    buff = list(map(int,input().split()))
    graph.append(buff)

# 방문 기록 만들기
visited=[]
for _ in range(N):
  visited.append([0 for _ in range(N)])

def bfs(x,y,graph):
    queue = deque()
    queue.append((x,y)) # 큐에 넣고 

    while queue : # 큐가 빌 때까지 
        x,y = queue.popleft() # 뺌
        visited[x][y]=1 # 방문 기록 
        W = graph[x][y] # 초기 값 
        dx = [W, 0]
        dy = [0, W]

        # 2개에 대한 방향
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간을 벗어났을 경우는 무시 
            if 0 > nx or nx >= N or 0 > ny or ny >= N :
                continue
            if visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                queue.append((nx,ny))

bfs(0,0,graph)

if visited[N-1][N-1]== 1: # 마지막에 방문할 수 있으면 
  print("HaruHaru")
else:
  print("Hing")