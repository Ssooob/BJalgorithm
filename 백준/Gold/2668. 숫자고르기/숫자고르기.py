import sys
input = sys.stdin.readline

N = int(input())			
arr = [0]				# 숫자 담을 리스트
for _ in range(N):
    arr.append(int(input()))
answer = set()				# 집합이라고 해서.. 집합자료형 

# dfs 정의
def dfs(first, second, num):
    first.add(num)			# 첫번째 줄 집합에 값 한 개씩 추가
    second.add(arr[num])		# 두번째 줄 집합에 값 한 개씩 추가
    if arr[num] in first:		# arr[num]이 첫번째 줄 집합에 있을 때
        if first == second:		# 첫번째 줄과 두번째 줄이 같으면
            answer.update(first)	# 여러 값 결과 업데이트
            return True
        return False
    return dfs(first, second, arr[num])	# 아니면 재귀

# dfs 실행
for i in range(1, N+1):
    if i not in answer:			# 무조건.. 실행시켜줘야해서..  
        dfs(set(), set(), i)

print(len(answer))
print(*sorted(list(answer)), sep='\n')
