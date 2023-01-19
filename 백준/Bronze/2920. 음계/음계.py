numbers = list(map(int,input().split()))
cnt = 0 
for i in range(0,len(numbers)-1) :
    if numbers[i]-numbers[i+1] == 1 :
        cnt += 1
    elif numbers[i]-numbers[i+1] == -1 :
        cnt -= 1
if cnt == -7 :
    print('ascending')
elif cnt == 7 :
    print('descending')
else :
    print('mixed')