ori_numbers = list(map(int,input().split()))
numbers = ori_numbers

while numbers != sorted(ori_numbers) :
    for i in range(len(numbers)-1):
        if numbers[i]> numbers[i+1] : 
            numbers2 = [numbers[i],numbers[i+1]]
            s_numbers2 = sorted(numbers2)   
            numbers [i] = s_numbers2[0]
            numbers [i+1] = s_numbers2[1]
            print(*numbers) 
        else :
            pass