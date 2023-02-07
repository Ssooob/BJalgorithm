T = int(input())
members = []
for _ in range(T):
    my_w,my_h = map(int,input().split())
    members.append((my_w,my_h)) # 자구 리스트 내 값이 변해서.. tuple로 풀었음
for i in range(T):
    my_data = members[i]
    rank = 1
    for j in range(T):
        if my_data[0] < members[j][0] and my_data[1] < members[j][1]:
            rank += 1 
    print(rank, end = " ")