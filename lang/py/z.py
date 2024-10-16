import random as r
l=['rock','paper','scissor']
h=int(input('''
1 : rock
2 : paper
3 : scissor
enter your choise : '''))
c=r.choice(l)
print('compuets move is : ',c)
if h==c :
    print('draw')
elif (h==1 and c=='scissor') or (h==2 and c=='rock') or (h==3 and c=='paper') :
    print('you win')
else:
    print('computer wins')