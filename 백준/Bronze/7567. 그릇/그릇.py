bowl = input() 
height = 10
for i in range(len(bowl)-1) :
    if bowl[i] != bowl[i+1]:
        height =  height + 10
    else : 
        height =  height + 5
print(height)