# 1085 직사각형에서 탈출

# 경계면으로만 가면되니까 기본 x,y값도 중요
# x,y값에서 경계면 상하좌우에서의 경계면
x,y,w,h = map(int,input().split())
print(min(x,y,w-x,h-y))
