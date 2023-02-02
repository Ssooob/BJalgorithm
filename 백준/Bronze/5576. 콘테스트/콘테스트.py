W,K = [],[]
for _ in range(10):
    W.append(int(input()))
for _ in range(10):
    K.append(int(input()))
Score_W = sorted(W,reverse=True)[0:3] 
Score_K = sorted(K,reverse=True)[0:3]
print(sum(Score_W),sum(Score_K))