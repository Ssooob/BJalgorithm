N = int(input())
balls_raw = list(map(int,input().split()))
balls = balls_raw

def dfs(depth,ball):
    global total,balls 
    
    # 조건식을 달아줘야하고..
    if depth == N-2 : 
        total.append(ball)
        #print(total)
        balls = balls_raw
        return
        # append 안 쓸거면 최대값 구하는 식 쓰고 

    # 기본 재귀식을 달아줘야하고.. 
    for i in range(1,len(balls)-1):
        next_ball = ball + (balls[i-1]*balls[i+1])
        b = balls.pop(i)
        dfs(depth+1,next_ball)
        # 복구해주는 작업이 꼭 필요함 
        balls.insert(i,b)

total = [] 
dfs(0,0)
print(max(total))