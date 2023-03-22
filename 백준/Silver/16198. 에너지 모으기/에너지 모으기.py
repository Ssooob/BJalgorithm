N = int(input())
balls_raw = list(map(int,input().split()))
balls = balls_raw

def dfs(depth,ball):
    global balls, max_ball
    
    # 조건식을 달아줘야하고..
    if depth == N-2 : 
        if ball >= max_ball :
            max_ball = ball 
        # balls = balls_raw 
        # 원래는 복구를 여기서 해줬는데.. 이건 의미가 없는 듯
        # 복구는 dfs 식 끝난 후에 해주기 
        # visited할 때도 dfs 전 후로 append pop 해주는 것처럼 
        return
    
    # 기본 재귀식을 달아줘야하고.. 
    for i in range(1,len(balls)-1):
        next_ball = ball + (balls[i-1]*balls[i+1])
        b = balls.pop(i)
        dfs(depth+1,next_ball)
        # 복구해주는 작업이 꼭 필요함 
        balls.insert(i,b)

max_ball = 0 
dfs(0,0)
print(max_ball)    
