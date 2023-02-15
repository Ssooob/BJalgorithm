import sys
sys.setrecursionlimit(10**9)
a,b = map(int,input().split())
cnt = 0 
def rect_cut(a,b):
    global cnt
    if a == b :
        cnt += 1
        return cnt
    else :
        if a > b :
            a -= b
            cnt += 1
            rect_cut(a,b)
        elif a < b :
            b -= a
            cnt += 1
            rect_cut(a,b)
rect_cut(a,b)
print(cnt)