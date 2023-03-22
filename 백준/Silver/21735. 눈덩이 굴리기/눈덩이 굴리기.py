N,M = map(int,input().split())
snows = list(map(int,input().split()))

# 컨셉.. 두 가지를 실행했을 때 더 크게 남는애를 선택하는게 낫지 않나? 
# max(1안, 2안 해서) 더하기 
# 모든 선택마다 

def dfs(depth): # , snow_idx
    global res, total, snows

    # 만약 시간이 됐다면 각 경우의 수에 대한 total값을 도출
    if depth == M : # or snow_idx == N-1: # 그리고 마지막꺼 골랐을 때 
        snow_idx,snow_val = -1,1
        for s in snow:
            # 0 0 0 0 1 
            if s == 0 :
                if snow_idx +1 < N : 
                    snow_idx += 1
                    snow_val += snows[snow_idx]
                    
                else :
                    break

            elif s == 1 :
                if snow_idx +2 < N : 
                    div_snow = int(snow_val//2)
                    snow_idx += 2
                    snow_val =  div_snow + snows[snow_idx]
                    
                else :
                    break
        # print(snow,snow_val)
        total.append(snow_val)

        return

    for i in range(2): # 0과 1의 경우에 수로 5번을 고를 거임 
        snow.append(i)
        dfs(depth+1) 
        snow.pop()


total,res = [],0
snow = []
dfs(0) # ,0
print(max(total)) 