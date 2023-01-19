nanta = input()
left = nanta.find('(')
right = nanta.find(')')
c_left = nanta[:left].count('@')
c_right = nanta[right:].count('@')

print(c_left, c_right)