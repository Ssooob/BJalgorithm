T = int(input())
result = list(map(int,input().split()))
total_score,score = 0,0
for t in range(T):
    if result[t] == 1:
        score += 1
        total_score += score
    elif result[t] == 0:
        score = 0
print(total_score)