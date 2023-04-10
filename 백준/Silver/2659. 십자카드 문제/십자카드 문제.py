nums = list(input().split())

def find_clock(nums):
    clocks_num = []
    for i in range(4):
        tmp = []
        for j in range(4):
            tmp.append(nums[(i+j)%4])
        clocks_num.append(int("".join(tmp)))
    min_clocks_num = min(clocks_num)

    return min_clocks_num
min_clocks_num = find_clock(nums)

cnt = 0
for i in range(1111,min_clocks_num+1):
    if '0' not in str(i):
        if i == find_clock(list(str(i))):
            cnt += 1
print(cnt)
