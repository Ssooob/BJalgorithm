T = int(input())
for t in range(T):
    rs = ''
    string = list(input().split())
    for s in string :
        rs += s [::-1] + ' ' 
    print(rs)