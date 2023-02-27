p,n = map(int,input().split())
members = []
rank_class = []
for _ in range(p):
    members.append(list(input().split()))

for m in members:
    # 첫 리스트 생성
    if len(rank_class) == 0 :
        rank_class.append([m[0],m])
    else :
        for i in range(len(rank_class)):
            event_flag= False
            if (len(rank_class[i]) < n+1) and (int(rank_class[i][0])-10) <= int(m[0]) <=(int(rank_class[i][0])+ 10) :
                # if len(rank_class[i]) == n+1:
                #     break
                rank_class[i].append(m)
                event_flag = True
            # 요소가 사용됐으면 종료
            if event_flag == True:
                break
        # 생성되어있는 리스트 안에 범위가 없다면, 새로 추가
        if event_flag == False :
            rank_class.append([m[0],m])

for j in rank_class:
    if len(j) == n + 1 :
        print('Started!')
    else :
        print('Waiting!')
    sorted_j = sorted(j[1:len(j)], key = lambda x : x[1])
    for k in sorted_j:
        print(*k)