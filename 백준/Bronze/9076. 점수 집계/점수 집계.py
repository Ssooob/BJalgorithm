T = int(input())
for t in range(T) :
    
    score = list(map(int,input().split()))
    del score[int(score.index(max(score)))]
    del score[int(score.index(min(score)))]

    if max(score)-min(score) >=4 :
        print("KIN")
    else :
        print(sum(score))