import sys
input = sys.stdin.readline
n = int(input())
in_cars = {}
out_cars = []
cars = 0

for i in range(n):
    in_cars[str(input().rstrip())] = i

for _ in range(n):
    out_cars.append(str(input().rstrip()))

for j in range(n - 1):
    for k in range(j + 1, n):
        if in_cars[out_cars[j]] > in_cars[out_cars[k]]:
            cars += 1
            break
print(cars)