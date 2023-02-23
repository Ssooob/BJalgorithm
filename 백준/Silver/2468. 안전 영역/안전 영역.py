import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline

N = int(input())
graph = []
max_buff,min_buff = [],[]
for _ in range(N):
    buff = list(map(int,input().split()))
    max_buff.append(max(buff)) # 원래는 min도 했었는데.. 아예 잠기지 않을 수 있다의 의미는 0을 의미하는 듯
    graph.append(buff)
max_val = max(max_buff)

def dfs(x,y,visited):
    if x <=-1 or x >=N or y <=-1 or y >= N :
        return False

    # 현재 노드를 아직 방문하지 않았다면?
    if visited[x][y] == 0 :
        # 해당 노드 방문 처리
        visited[x][y] = 1
        # 상,하,좌,우 재귀적으로 호출
        dfs(x+1,y,visited)
        dfs(x,y+1,visited)
        dfs(x-1,y,visited)
        dfs(x,y-1,visited)
        return True
    return False

# 잠긴부분 1 안 잠긴 부분 0으로 만들기 
total_result = []
for th in range(0,max_val):
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] <=th:
                visited[i][j] = 1
    #print(th, visited)
    # 모든 노드에 대해서  
    result = 0 
    for i in range(N):
        for j in range(N):
            if dfs(i,j,visited) == True:
                result += 1
    total_result.append(result)
#print(total_result)
print(max(total_result))