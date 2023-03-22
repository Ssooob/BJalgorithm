import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int,input().split()))
op = list(map(int,input().split()))
res_max,res_min = -1e9,1e9
def dfs(depth,number,pl,mi,mu,di):
    global res_min, res_max
    if depth == N :
        if number > res_max :
         res_max = number
        if number < res_min : 
         res_min = number
         return
    if pl >= 1 :
        dfs(depth+1,number+nums[depth],pl-1,mi,mu,di)
    if mi >= 1 :
        dfs(depth+1,number-nums[depth],pl,mi-1,mu,di)
    if mu >= 1 :
        dfs(depth+1,number*nums[depth],pl,mi,mu-1,di)
    if di >= 1 :
        dfs(depth+1,int(number/nums[depth]),pl,mi,mu,di-1)
dfs(1,nums[0],op[0],op[1],op[2],op[3])
print(res_max)
print(res_min)