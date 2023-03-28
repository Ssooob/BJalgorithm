N = int(input().rstrip())
A = list(map(int,input().split()))
M = int(input().rstrip())
B = list(map(int,input().split()))


def bi_s(array,target,start,end):

    # 끝날 때까지 
    while start <= end : # start idx가 end idx보다 작은 경우만 

        # 중간값 계산
        mid = int((start+end)/2) # 중간 idx를 탐색

        if array[mid] == target : # array[중간 idx] -> value & targrt(value)
            return 1
        
        elif array[mid] > target :
            end =  mid-1 # mid & end는 idx 
        else :
            start =mid + 1

    return 0 # 이 안에 안 나오면, 0 return


array = sorted(A)
for i in B:
    print(bi_s(array,i,0,N-1))