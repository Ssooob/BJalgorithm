import sys
input = sys.stdin.readline
left = list(input().rstrip())
right = []

for _ in range(int(input())):
    order = list(input().split())
    if order[0] == 'L' and left:
        right.append(left.pop())
    elif order[0] == 'D' and right:
        left.append(right.pop())
    elif order[0] == 'B' and left:
        left.pop()
    elif order[0] == 'P':
        left.append(order[1])
left.extend(reversed(right))
print(''.join(left))