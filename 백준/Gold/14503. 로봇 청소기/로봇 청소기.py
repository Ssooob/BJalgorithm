

n,m = map(int,input().split())
x,y,d= map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [-1,0,1,0] # 북동남서
dy = [0,1,0,-1]

visited[x][y] = 1
cnt = 1
while True:
    flag = False
    # 4칸을 돌면서
    for _ in range(4):
        # 0,3,2,1로 만들어주기 위한 식
        d = (d + 3) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        # 청소한다
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 :
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                x,y = nx, ny
                cnt += 1
                flag = True
                break
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if flag == False :
        if graph[x - dx[d]][y - dy[d]] == 1 :
            print(cnt)
            break
        else :
            x,y = x - dx[d], y - dy[d]

