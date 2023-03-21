def dfs():
    
    # 조건을 만족하면 해당 문을 return
    if len(stack)== m : # 길이가 맞으면 
        print(' '.join(map(str,stack))) # print
        return
    
    # 방문하지 않았을 경우에만 방문해주도록 
    for i in range(1, n+1): # 1,2,3,4
        if visited[i] :  #  visited가 True일 때
            continue # 아래 코드를 실행하지 않고 건너뜀 
        visited[i] = True # False라면 True로 바꾸고
        stack.append(i) # stack에 하나 쌓고.. 
        dfs() # 다시 호출
        stack.pop() # 안에 있는거 지우고 
        visited[i] = False # 다시 False로 만들기 (나머지 것들도 있으니까)

n,m = map(int,input().split())
stack = []
visited = [False]*(n+1)
dfs()