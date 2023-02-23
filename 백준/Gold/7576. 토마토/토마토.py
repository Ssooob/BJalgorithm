from collections import deque
m,n = map(int,input().split())

# 2차원 그래프 받기 
graph = [list(map(int, input().split())) for _ in range(n)]
# print(graph)

# 4 방향으로 나갈 수 있게 
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 정답이 담길 변수
result = 0

def bfs(): # 원래는.. 시작점을 넣어야하는데, 시작점이 여러개인 경우가 있어서 뺐음
    # 큐 만들기 
    queue = deque()
    # 토마토 시작점 찾기
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append([i, j])

    while queue :
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나면 안되고, 빈공간도 안됨 
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                # 익히고, 이전꺼에 1을 더해서 나오기 
                graph[nx][ny] = graph[x][y] + 1 
                queue.append((nx,ny))

bfs()
for i in graph: # 리스트 
    for j in i: # 리스트 당 한 원소 
        # 토마토를 익히지 못했다면 -1 출력
        if j == 0:
            print(-1)
            exit(0) # 아예 나가버리기 
    # 다 익혔다면 최댓값이 정답
    result = max(result, max(i))
# 처음 시작을 1로 표현했으니 1을 뺌
print(result - 1)