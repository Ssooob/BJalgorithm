c = int(input())
candidate = []
for i in range(c):
    candidate.append(int(input()))
#print(candidate)
if len(candidate) > 1 :    
    mine,others = candidate[0],candidate[1:]
    vote = 0
    sorted_others = sorted(others,reverse=True)
    while True:
        sorted_others.sort(reverse=True)
        #print(mine)
        #print(sorted_others)
        if mine <= sorted_others[0]:
            #print(sorted_others[0])
            mine +=1
            sorted_others[0] -=1
            vote +=1
            # print(mine)
            # print(sorted_others)
        else:
            break 
    print(vote)
else :
    print(0)