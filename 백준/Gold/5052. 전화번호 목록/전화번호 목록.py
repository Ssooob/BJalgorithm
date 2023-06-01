import sys
input = sys.stdin.readline

t = int(input())
for tt in range(t):
    flag = True
    numbers = int(input())
    n_books = sorted([input().rstrip() for _ in range(numbers)])
    
    for nb in range(numbers-1):
        if n_books[nb] == n_books[nb+1][:len(n_books[nb])]:
            print('NO')
            break
    else :
        print('YES')