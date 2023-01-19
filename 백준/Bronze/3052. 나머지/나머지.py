numbers= []
for i in range (10):
    a = int(input())% 42
    numbers.append(a)
print(len(set(numbers)))