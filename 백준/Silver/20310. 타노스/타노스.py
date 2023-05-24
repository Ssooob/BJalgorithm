num = list(input())
len_0,len_1 = 0,0
str_0,str_1 = '0','1'
for n in num:
    if n == '0':
        len_0 += 1
    elif n == '1':
        len_1 += 1
res = str_0*int(len_0/2) + str_1*int(len_1/2)
print(res)