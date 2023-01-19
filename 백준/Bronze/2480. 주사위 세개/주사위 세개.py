num_list = list(map(int,input().split()))
num_list1 = list(set(num_list))
if len(num_list1) == 1 :
    own = int(num_list1[0])*1000 + 10000
elif len(num_list1) == 3 :
    own = max(num_list1)*100
else :
    for i in range(3):
        if num_list.count(num_list[i]) ==2 :
            num = int(num_list[i])
            break
    own = int(num)*100 + 1000
    
print(own)