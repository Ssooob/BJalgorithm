def dfs():
    # 조건식
    if len(stack) == m :
        s_stack = sorted(stack) # 정렬
        if s_stack not in stack1 : # 만약 stack1에 없으면 
            print(' '.join(map(str,s_stack))) #걔네들만 출력
            stack1.append(s_stack) # 저장
        return

    # dfs 식
    for i in range(1,n+1):
        # 중복 없는 애를 골라야함
        if visited[i] :
            continue # True일 경우에 밑에 식 작동 안하도록
        visited[i] = True
        stack.append(i)
        dfs()
        stack.pop()
        visited[i] = False


n,m = map(int,input().split())
visited = [False]*(n+1)
stack,stack1 = [],[]
dfs()