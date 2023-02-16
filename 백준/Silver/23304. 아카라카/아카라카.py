import sys
sys.setrecursionlimit(10**9)
s = sys.stdin.readline().rstrip()

def aka_pel(s):
    P_flag = False
    len_s = len(s)

    if len_s == 1:
        P_flag = True
        return P_flag
    
    if s == s[::-1]:
        P_flag = aka_pel(s[:len_s//2])
    
    return P_flag


if aka_pel(s):
    print('AKARAKA')
else:
    print('IPSELENTI')