numbers = list(map(int,input()))

zero = []
one = []
cnt = 0
for i in range(int(len(numbers))-1):
    if numbers[i] != numbers[i+1] :  
        cnt += 1  

print((cnt + 1) // 2)