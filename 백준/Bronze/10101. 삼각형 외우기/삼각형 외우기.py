tri = [0]*3
for t in range(3):
   tri[t] = int(input())

#print(set(tri))
if sum(tri) == 180 :
    if len(set(tri)) == 1:
        print("Equilateral")
    elif len(set(tri)) == 2:
        print("Isosceles")
    elif len(set(tri)) == 3:
        print("Scalene")

else :
    print("Error")