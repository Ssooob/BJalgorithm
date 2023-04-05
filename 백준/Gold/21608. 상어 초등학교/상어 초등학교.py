n = int(input())
stu = {}
for _ in range(n*n):
    temp = list(map(int,input().split()))
    stu[temp[0]] = temp[1:]
graph = [[0]*n for _ in range(n)]
#  print(list(stu[2]))

# 4방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#  학생 수 만큼 돌면서 자리 앉혀줌
for order in list(stu.keys()):
    # print(order)
    tmp = [] #  가능한 자리 넣어줄 list
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0 : # 비어있으면
                like = 0 
                blank = 0 
                for k in range(4):
                    nx, ny = i+dx[k], j +dy[k]
                    if (0<= nx < n) and (0<= ny < n):
                        if graph[nx][ny] in list(stu[order]):
                            like += 1
                        if graph[nx][ny] == 0 :
                            blank += 1
                tmp.append([like,blank,i,j]) # 정렬을 위한 조건
    tmp = sorted(tmp, key = lambda x : (-x[0], -x[1], x[2], x[3]))
    graph[tmp[0][2]][tmp[0][3]] = order
    # print(graph)

# 만족도 구하는 함수
likes = 0
for i in range(n):
    for j in range(n):
        order = graph[i][j]
        sum_like = 0
        for k in range(4):
            nx,ny = i + dx[k], j + dy[k]
            if ( 0<= nx < n) and (0 <= ny < n):
                if graph[nx][ny] in list(stu[order]):
                    sum_like += 1
        if sum_like == 0 :
            likes += sum_like
        else :
            likes += 10**(sum_like-1)
print(likes)