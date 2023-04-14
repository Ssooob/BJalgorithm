
n = int(input())
members = []
for i in range(n):
    age, name = map(str,input().split())
    members.append([int(age),i,name])


sort_members = sorted(members, key = lambda x : (x[0],x[1]))
for s in sort_members :
    print(s[0],s[2])
