while True :
    num = list(map(int,input().split()))
    if sum(num) == 0:
        break
    max_val = max(num)
    num.remove(max_val)
    if max_val*max_val == num[0]*num[0] + num[1]*num[1] :
         print('right')
    else :
        print('wrong')