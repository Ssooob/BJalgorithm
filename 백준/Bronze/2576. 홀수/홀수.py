numbers = []
sum = 0
for t in range(7):
    num = int(input())
    if num % 2 != 0:
        sum += num
        numbers.append(num)
if sum == 0:
    print(-1)
else :    
    print(sum)
    print(min(numbers))