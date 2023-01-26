Q,D,N,P = 25, 10, 5, 1
T = int(input())
for t in range(T):
    charge = int(input())
    nQ = charge//Q 
    charge = charge%Q
    nD = charge//D 
    charge = charge%D 
    nN = charge//N 
    charge = charge%N
    nP = charge//P 
    charge = charge%P

    print(nQ, nD, nN, nP)
