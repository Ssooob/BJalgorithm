voca = input()
len_voca = len(voca)
result = []
# 합이 7인 조합들
for i in range(1,len_voca-1):
    for j in range(i+1,len_voca):
        ans = (voca[:i][::-1])+(voca[i:j][::-1])+(voca[j:][::-1])
        result.append(ans)
result.sort()
print(result[0])