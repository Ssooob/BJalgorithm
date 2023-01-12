numbers = list(map(int,input()))

zero = []
one = []
new=[]
for i in range(int(len(numbers))-1):
    if numbers[i] != numbers[i+1] :    
        # 0에서 1로 바뀐 경우
        if numbers[i] == 0:
            zero.append(i)
        # 1에서 0으로 바뀐 경우
        elif numbers[i] == 1:
            one.append(i)
#total = zero + one # 4 4
#total.sort() # [1, 3, 5, 7, 9, 11, 13, 18]
print(max(len(zero),len(one)))