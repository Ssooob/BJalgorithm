while True :
    line = input()
    cnt =  0
    # 코드 끝나는 조건 -> 얘가 있으면 코드가 아예 종료이기 때문에, 함수가 상단에 위치해야함
    if line == '#':
        break
    for i in line :
        if i in 'aeiouAEIOU' : # 이런식으로 묶어서 받아도 됨
            cnt +=1
    print(cnt)