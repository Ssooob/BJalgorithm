T = int(input())
for t in range(1,T+1):
    R,S = input().split()
    new_string = ''
    for s in S: # 이렇게 하면 s는 S의 요소가 됨
        new_string += int(R)*s

    print(new_string)