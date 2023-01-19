a = int(input())
b = int(input())
sum= 0
idx = []
for num in range(a,b+1) :
    cnt = 0
    if num > 1 :
        for n in range(2,num) :
            if num % n == 0 :
                cnt +=1
        if cnt == 0:
            sum+=num
            idx.append(num)
if sum == 0 : 
    print(-1)
else :
    print(sum)
    print(idx[0])
