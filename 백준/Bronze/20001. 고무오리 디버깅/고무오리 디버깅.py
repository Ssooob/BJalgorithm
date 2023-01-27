duck= []
problem = 0
while 1 :
    duck = input()
    if duck == "문제":
        problem +=1 
    elif duck == "고무오리":
        if problem >=1:
            problem-=1
        else :
            problem +=2
    if duck == "고무오리 디버깅 끝":
        break
if problem == 0:
    print("고무오리야 사랑해")
else :
    print("힝구")
