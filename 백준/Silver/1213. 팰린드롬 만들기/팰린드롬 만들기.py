pel = input()
# 글자 요소 수 세기 
pel_cnt = [0 for _ in range(26)]
for p in pel:
    pel_cnt[ord(p)-65] += 1

odd =0 
odd_alpha = ''
alpha = ''

for i in range(26):
    if pel_cnt[i] % 2 == 1 :
        odd +=1
        odd_alpha += chr(i+65)
    alpha += chr(i+65)*(pel_cnt[i]//2)

if odd > 1:
    print("I'm Sorry Hansoo")
else : 
    print(alpha + odd_alpha + alpha[::-1])