sentence = input()
ord_str = ''
Up = [i for i in range(65,91)]
Down = [i for i in range(97,123)]
Upper = Up+Up
Downer = Down+Down
for s in sentence :
    if 65 <= ord(s) <= 90 :
        ord_s = chr(Upper[(ord(s)-ord('A'))+13])
    elif 97 <= ord(s) <= 122 :
        ord_s = chr(Downer[(ord(s)-ord('a'))+13])
    else :
        ord_s = s 
    ord_str += ord_s
print(ord_str)