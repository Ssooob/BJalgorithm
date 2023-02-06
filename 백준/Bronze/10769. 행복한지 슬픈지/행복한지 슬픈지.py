string = input()
happy,sad,none = 0,0,0
emotion = []
cnt = 0
for i in range(len(string)-2) :
    if string[i] == ':' and string[i+1] == '-' :
        if string[i+2] == ')':
            happy += 1
        elif string[i+2] == '(':
            sad += 1
if happy == 0 and sad == 0:
    result = 'none'
else :
    if happy > sad :
        result = 'happy'
    elif sad > happy :
        result = 'sad'
    elif sad == happy :
        result = 'unsure'
print(result)
        