T = int(input())
numbers = []
for t in range(T) :
    num = int(input())
    numbers.append(num)
s_numbers = sorted(numbers)
for s in s_numbers :
    print(s)