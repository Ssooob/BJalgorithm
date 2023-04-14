n = int(input())
end = 48*60
team1 = 0
team2 = 0
win = 0

for _ in range(n):
    team, goal = input().split()
    min, sec = map(int, goal.split(':'))
    time = min*60 + sec
    
    if team == '1':
        if win == 0:
            team1 += (end - time)
        win += 1
        if win == 0:
            team2 -= (end - time)
    else:
        if win == 0:
            team2 += (end - time)
        win -= 1
        if win == 0:
            team1 -= (end - time)
            
print('{:0>2}:{:0>2}'.format((team1)//60, (team1)%60))
print('{:0>2}:{:0>2}'.format((team2)//60, (team2)%60))