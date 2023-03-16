import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement


a = int(input())
sets = [1,5,10,50]

data = list(combinations_with_replacement(sets, a)) 

cand = []
for i in data :
    sum_i = sum(i)
    cand.append(sum_i)
print(len(set(cand)))