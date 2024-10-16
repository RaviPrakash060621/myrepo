print('''\nWelcom you to - tic tac toe - game''')

import random  as r
l=['A','B','C','D','E','F','G','H','I']
l1=['A','B','C','D','E','F','G','H','I']
m=['X','O']
def p():
            print('''
                 |      |    
               {} |   {}  |  {} 
            _____|______|______
                 |      |    
               {} |   {}  |  {} 
            _____|______|______
                 |      |    
               {} |   {}  |  {} 
                 |      |    '''.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8]))
 #             win logic
def win(l):
            if (l[0]==l[1]==l[2]==h) or (l[3]==l[4]==l[5]==h) or (l[6]==l[7]==l[8]==h):
                return 1
            elif (l[0]==l[3]==l[6]==h) or (l[4]==l[1]==l[7]==h) or (l[8]==l[5]==l[2]==h):
                return 1
            elif (l[0]==l[4]==l[8]==h) or(l[6]==l[4]==l[2]==h):
                return 1
            
            elif (l[0]==l[1]==l[2]==c) or (l[3]==l[4]==l[5]==c) or (l[6]==l[7]==l[8]==c):
                return 0
            elif (l[0]==l[3]==l[6]==c) or (l[4]==l[1]==l[7]==c) or (l[8]==l[5]==l[2]==c):
                return 0
            elif (l[0]==l[4]==l[8]==c) or(l[6]==l[4]==l[2]==c):
                return 0

while True:
    game=input('''\nPress 1 to play the game.
Press 2 to exit.
''')
    if game=='1':
        h=m[0]
        c=h1=m[1]
        l=['A','B','C','D','E','F','G','H','I']
        l1=['A','B','C','D','E','F','G','H','I']
        m=['X','O']        
        while True:
            mode=(input('''
Select mode :-
\n    1: Player vs Player
    2: Player vs Computer
\nEnter your choice :'''))
            if mode=='1':
                while True:
                    s=(input('''
Choose Player 1 sign.
    1 : X
    2 : O
Enter your choice :'''))
                    if s=='1':
                        break
                    elif s=='2':
                        h=m[1]
                        h1=m[0]
                        break
                    else:
                        print('Invalid choice')
                p()  
                for i in range(5):
                #         players 1 turn  
                        while True:
                            u=input('Player 1 :- {} turn : '.format(h))
                            u=u.upper()
                            if u not in l1:
                                print('Invalid move')    
                            else:
                                l1.remove(u)
                                break
                        l[ord(u)-65]=h
                        
                        if i>=2:
                            w=win(l)
                            if w==1:
                                p()
                                print('\nPlayer 1 :- {} win  :) '.format(h))
                                break
                            elif i==4:
                                print('\nMatch draw')
                                p()
                                break
                        p()
                #         players 2 turn  
                        while True:
                            u=input('Player 2 :- {} turn : '.format(h1))
                            u=u.upper()

                            if u not in l1:
                                print('Invalid move')    
                            else:
                                l1.remove(u)
                                break
                        l[ord(u)-65]=h1
                        p()
                        if i>=2:
                            w=win(l)
                            if w==0:                           
                                    print('\nPlayer 2 :- {} win  :) '.format(h1))
                                    break
                break
            elif mode=='2':
                s=(input('''
Choose your sign.
    1 : X
    2 : O
Enter your choice :'''))
                while True:
                    if s=='1':
                        break
                    elif s=='2':
                        h=m[1]
                        h1=m[0]
                        break
                    else:
                        print('Invalid choice')
                p()
                for i in range(5):
                #         players turn  
                        while True:
                            u=input('Your turn : ')
                            u=u.upper()

                            if u not in l1:
                                print('Invalid move')    
                            else:
                                l1.remove(u)
                                break
                        l[ord(u)-65]=h

                        if i>=2:
                            w=win(l)
                            if w==1:
                                p()
                                print('\nYou win  :) ')
                                break
                            elif i==4:
                                p()
                                print('\nMatch draw')
                                break
                #                    computers turn
                        ch=r.choice(l1)
                        print('Computers turn : ',ch)
                        l1.remove(ch)
                        l[ord(ch)-65]=c
                        p()

                        if i>=2:
                            w=win(l)
                            if w==0:
                                print('\nComputer win')
                                break
                break
            else:
                print('Invalid entry')

    elif game=='2':
        break
    else:
        print('Invalid entey')