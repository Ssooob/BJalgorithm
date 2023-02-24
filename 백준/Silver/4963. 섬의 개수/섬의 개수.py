import sys
sys.setrecursionlimit(10**6)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs (x,y):
    # 방문 처리 
    visited[x][y] = True

    # 4 방향을 전부 고려할 for문
    for i in range(8) : 
        nx = x + dx[i]
        ny = y + dy[i] 
    
        # 범위에서 벗어난 것은 제외 
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1 and visited[nx][ny]== False:
            dfs(nx,ny)
            #return True
        #return False
    return

while True : 
    result = 0 
    w,h = map(int,input().split())
    if w == 0 and h == 0 :
        break
    graph = [list(map(int,input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]

    for x in range(h):
        for y in range(w):
            if visited[x][y] == False  and graph[x][y] == 1 :
                dfs(x,y)
                result += 1
    print(result)