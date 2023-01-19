N = int(input())
scores = list(map(int,input().split()))
M = max(scores)
new_score = []
for i in scores:
    new_score.append((i/M)*100)
avg_score = (sum(new_score))/N
print(avg_score)