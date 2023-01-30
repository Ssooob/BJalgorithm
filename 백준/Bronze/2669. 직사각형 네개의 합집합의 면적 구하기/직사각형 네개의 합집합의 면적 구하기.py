matrix = [[0]*100 for _ in range(100)]
max_x = 0
for _ in range(4):
    squa = list(map(int,input().split()))
    for x in range(squa[0],squa[2]) :
        #if max(squa[0],squa[2])>= max_x:
            #max_x = max(squa[0],squa[2])
        for y in range(squa[1],squa[3]):
            matrix[x][y] = 1

sum_m = 0
for i in range(100):
    sum_m+= sum(matrix[i])
print(sum_m)