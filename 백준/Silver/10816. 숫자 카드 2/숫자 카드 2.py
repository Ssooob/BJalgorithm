import sys
input = sys.stdin.readline

N = int(input().rstrip())
array = sorted(list(map(int,input().split())))
M = int(input())
M_nums = list(map(int,input().split()))

def bi_sear(array,target,start,end) : 
    cnt = 0 
    while start <= end :
        mid = int((start+end)/2)
        if array[mid] == target:
            for i in range(mid,start-1,-1) :
                if array[i] == target:
                    cnt += 1
                else :
                    break
            for j in range(mid+1,end+1):
                if array[j] == target:
                    cnt += 1
                else :
                    break
            return cnt  
        elif array[mid] > target:
            end = mid-1
        else :
            start = mid + 1
    return 0
d = {}
for m in M_nums:
    if m not in d:
        d[m] = bi_sear(array,m, 0,N-1)
print(' '.join(str(d[m]) if m in d else '0' for m in M_nums))
