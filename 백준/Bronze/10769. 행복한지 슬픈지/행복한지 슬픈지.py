string = input()
happy_cnt = string.count(':-)')
sad_cnt = string.count(':-(')
if happy_cnt > sad_cnt :
    print('happy')
elif happy_cnt < sad_cnt :
    print('sad')
elif happy_cnt == sad_cnt == 0 :
    print('none')
elif happy_cnt == sad_cnt :
    print('unsure')