call = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
string = list(input())
sec = 0
for i in string :
    for j in call :
        if i in j : 
            dial = call.index(j) +3
            sec += dial
print(sec)