num = int(input())
card = [i for i in range(1,num+1)]
remove = []
for _ in range(len(card)):
    a = card.pop(0)
    remove.append(a)
    if len(card)>=2:
        b = card.pop(0)
        card.append(b)
print(*remove)