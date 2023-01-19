T = int(input())
sum = 0
for t in range(T):
    # 0은 안귀여움, 1은 귀여움
    a = int(input())
    sum += a
if sum >=(T+1)/2: 
    print("Junhee is cute!")
else :
    print( "Junhee is not cute!")