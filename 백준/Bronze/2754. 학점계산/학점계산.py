score = list(input())
standard = {
    "A" : 4.0,
    "B" : 3.0,
    "C" : 2.0,
    "D" : 1.0,
    "F" : 0.0
}
if len(score) >= 2 :
    if score[1] == '+':
        print(standard[score[0]]+0.3)
    elif score[1] == '-':
        print(standard[score[0]]-0.3)
    else :
        print(standard[score[0]])
else :
    print(standard[score[0]])