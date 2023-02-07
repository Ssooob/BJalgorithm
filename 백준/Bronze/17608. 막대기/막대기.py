import sys
input = sys.stdin.readline

T = int(input())
bars = []
for _ in range(T):
    bars.append(int(input()))
max_bar = bars[-1]
reverse_bar = bars[::-1]
cnt = 1
for b in reverse_bar:
    if b > max_bar :
        cnt += 1
        max_bar = b  
print(cnt)