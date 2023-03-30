
n,m = map(int,input().split())
data = list(map(int,input().split()))

num = sum(data)

start = 0 
end = num
result = num

while start<=end:
    mid = (start+end) // 2 
    if mid < max(data):
        start = mid + 1
        continue
    cnt,tmp =1,0
    for i in range(len(data)):
        if tmp + data[i] <= mid:
            tmp += data[i]
        else:
            tmp = data[i]
            cnt += 1
    if cnt <= m:
        end = mid - 1
        result = min(result,mid)
    else:
        start = mid + 1
print(result)