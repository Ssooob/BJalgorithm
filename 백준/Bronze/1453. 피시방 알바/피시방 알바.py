N = int(input())
seat = list(map(int,input().split()))
seat100 = [0]*101
cnt = 0
for i in seat :
    if seat100[i] != 0 :
        cnt += 1
    else :
        seat100[i] += 1
print(cnt)
