t = int(input())
for tt in range(t):
    break_flag = False
    blank = list(input())
    stack = []
    for b in range(len(blank)):
        if blank[b] == '(':
            stack.append('(')
        elif  blank[b] == ')':
            if len(stack) != 0 :
                stack.pop()
            else :
                print('NO')
                break_flag = True
                break
    if break_flag == False:
        if len(stack) == 0 :
            print('YES')
        else :
            print('NO')