string = input()
croat = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cro_cnt = 0
for i in croat:
    string = string.replace(i,"#")
print(len(string))