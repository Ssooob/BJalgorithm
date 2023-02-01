from itertools import combinations, permutations

N,M = map(int,input().split())
numbers = list(map(int,input().split()))

#combi = list(combinations(numbers, 3))
combi_sum = list(map(sum,list(combinations(numbers, 3))))
min,idx = M,0

for x in combi_sum:
    if x <= M :
        if M-x < min :
            min = M-x
            min_idx = idx
    idx += 1
print(combi_sum[min_idx])