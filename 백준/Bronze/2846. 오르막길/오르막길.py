N = int(input())
road = list(map(int,input().split()))
total_distance = []
distance = 0
for r in range(N-1):
    if road[r]<road[r+1]:
        distance += road[r+1]-road[r]
    else :
        total_distance.append(distance)
        distance = 0
total_distance.append(distance) # 마지막값
print(max(total_distance))
