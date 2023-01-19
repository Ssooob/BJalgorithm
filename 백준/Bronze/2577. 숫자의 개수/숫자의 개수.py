mul = 1
for i in range(3):
    num = int(input())
    mul *= num
mult = list(str(mul))
nums= [0]*10
for i in range(10):
    nums[i] = mult.count(str(i))
    print(nums[i])