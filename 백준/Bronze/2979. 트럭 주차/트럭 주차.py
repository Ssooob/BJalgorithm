cost = list(map(int,input().split()))

# 24시간에 대한 빈 배열 생성
time_100 = [0 for j in range(100)]
#print(time_24)

for c in range(3):
    a,b = map(int,input().split())
    for cc in range(a,b) : 
        time_100[cc] += 1
#print(time_100)
total_count = (time_100.count(1))*cost[0] + (time_100.count(2))*cost[1]*2 + (time_100.count(3))*cost[2]*3
print(total_count)
