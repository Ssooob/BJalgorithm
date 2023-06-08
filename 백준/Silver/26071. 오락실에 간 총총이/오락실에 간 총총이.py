import sys; input = sys.stdin.readline

N = int(input())
matrix = [input().strip() for _ in range(N)]

li = lj = N # i, j의 최소
ui = uj = -1 # i, j의 최대

# 곰곰이가 나올 때마다 최소와 최대를 갱신한다.
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'G':
            if li > i:
                li = i
            if ui < i:
                ui = i
            if lj > j:
                lj = j
            if uj < j:
                uj = j

# 곰곰이가 한 줄에 있으면. 즉, 최대와 최소가 같다면 그 수직 방향으론 움직일 필요가 없는 것이다.
# 아니면, 맨 끝으로 몰아야 할 수 밖에 없다.
# 최대 위치에서 0으로 몰던지 최소 위치에서 N - 1로 몰던지 해야 한다.

answer = 0
if li != ui:
    answer += min(ui, N - 1 - li)
if lj != uj:
    answer += min(uj, N - 1 - lj)
print(answer)