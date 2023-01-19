avg_score = [40]*5
for i in range(5):
    score = int(input())
    if score >= 40:
        avg_score[i] = score
print(int((sum(avg_score))/5))
