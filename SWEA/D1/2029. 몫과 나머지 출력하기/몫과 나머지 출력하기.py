T = int(input())

for t in range(1,T+1):
    a,b = list(map(int,input().split()))

    result1 = a//b
    result2 = a%b

    print(f"#{t} {result1} {result2}")