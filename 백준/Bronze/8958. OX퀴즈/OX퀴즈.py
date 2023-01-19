T = int(input())
for t in range(0,T): 
    ox = input()
    count, cont_count = 0,0
    for o in ox :
        if o == 'O':
            cont_count +=1
            count += cont_count
        elif o == 'X':
            cont_count = 0
    
    print(count)