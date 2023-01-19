T = int(input())
for t in range(T):
    k = int(input())  
    n = int(input())  
    home = [[(j+1) for j in range(n)] for i in range(k+1)]
   
    for i in range(1,k+1): # k-1 층에 대한 사람 (1층부터)
        for j in range(n): # 호수에 대한 사람 (1호부터)
            home[i][j] = sum(home[i-1][:j+1])
    print(home[k][n-1])