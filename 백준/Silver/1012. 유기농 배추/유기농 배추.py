import sys
sys.setrecursionlimit(10000)
t = int(input())
for T in range(t):
    n,m,p = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for _ in range(p):
        v1,v2 = map(int,input().split())
        graph[v1][v2] = 1

    def dfs(x,y):
        # 특정한 노드를 방문한 뒤에 연결된 노드들도 방문

        if x <=-1 or x >=n or y <=-1 or y >= m :
            return False

        # 현재 노드를 방문하지 않았다면 
        if graph[x][y]== 1 :
            # 해당 노드 방문 처리
            graph[x][y] = 0

            # 상,하,좌,우 모두 재귀적으로 호출
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x-1,y)
            dfs(x,y-1)

            return True
        return False

    # 모든 노드에 대해 탐색
    result = 0 
    for i in range(n):
        for j in range(m):
            # 현재 위치에서 DFS 수행
            if dfs(i,j) == True :
                result += 1
    print(result)