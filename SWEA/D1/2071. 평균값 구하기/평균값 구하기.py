T = int(input())
for t in range(1,T+1):
    numbers = list(map(int,input().split()))
    aver = round(sum(numbers)/len(numbers))

    print(f"#{t} {aver}")