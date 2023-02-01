h, m = map(int,input().split())
time = int(input())
mm = m + time 

if mm > 59:
    hh = mm//60
    h += hh
    mm -= 60*hh
    if h > 23 :
        hhh = h//24
        h -= 24*hhh
print(h,mm)