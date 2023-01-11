num = int(input())
N = num
count = 0 
while True :
    lnum = num//10 # 2
    rnum = num%10  # 6
    lsnum = (rnum + lnum)%10 # 8 
    num = (rnum*10) + lsnum # 68
    count += 1
    if num == N:
        break
print(count)