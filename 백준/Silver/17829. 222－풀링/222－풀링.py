m = int(input())
matrixs = [list(map(int,input().split())) for _ in range(m)]

def find_2nd(m,arr):
    if m == 1 :
        return print(arr[0][0])
    new_arr = [[]for _ in range(m//2)]
    
    for i in range(0,m,2):
        for j in range(0,m,2):
            new_arr[i//2].append(sorted([arr[i][j],arr[i][j+1],arr[i+1][j],arr[i+1][j+1]])[2])
    
    return find_2nd(m//2, new_arr)
find_2nd(m,matrixs)