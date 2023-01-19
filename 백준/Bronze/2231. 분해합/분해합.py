N = (int(input()))
result = 0
for i in range(1,N+1):
    nums = list(map(int,str(i)))
    A = sum(nums) + i
    if N == A :
        result=i
        break
print(result)
