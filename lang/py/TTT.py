import random  as r
l=['A','B','C','D','E','F','G','H','I']
l1=['A','B','C','D','E','F','G','H','I']
m=['X','O']

h=m[0]
c=m[1]
s=int(input('''Choose your sign.
1 : X
2 : O
Enter your choice :'''))
if s==2:
    h=m[1]
    c=m[0]
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
#             printing 
print('Enter your move')
def p():
    print('''
                 |      |    
               {} |   {}  |  {} 
            _____|______|______
                 |      |    
               {} |   {}  |  {} 
            _____|______|_____
                 |      |    
               {} |   {}  |  {} 
                 |      |    '''.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8]))
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
                print('\nMatch draw')

        if i==4 :
            p()
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