N = int(input())
while N !=1 :
    for i in range(2,N+1): # 소인수 분해는 2부터 N까지
        if N%i == 0:
            print(i)
            N = N//i
            break