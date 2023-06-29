def solution(prices):
    answer =[0] * len(prices)
    for i in range(len(prices)):
        stop_flag = False 
        for j in range(i+1, len(prices)):
            if stop_flag == True :
                break
            if prices[i] <= prices[j]:
                answer[i]+=1
            else:
                answer[i]+=1
                stop_flag = True
    return answer