T = int(input())
num_list = []
for t in range(T):
    num = int(input())
    if num == 0 :
        num_list.pop(len(num_list)-1)
    else :
        num_list.append(num)
print(sum(num_list))