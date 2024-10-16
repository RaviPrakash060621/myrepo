#This is TIC-TAC-TOE developed by spdf

box = [['1','2','3'],['4','5','6'],['7','8','9']]
box2 = ['1','2','3','4','5','6','7','8','9']

def board(box,player1,player2,p1sign,p2sign):
    for i in range(3):
        for j in range(3):
            print(box[i][j], end = " ")
            if j<2:
                print(" | ",end="")
        if i<2:
            print('\n___|____|___')
        else:
            print('\n   |    |   ')
    print(player1,': ',p1sign,'        ',player2,': ',p2sign)

def insert(a,positon,sign):
    for i in range(3):
        for j in range(3):
            if positon == a[i][j]:
                a[i][j]= sign
    return a
def move_check(move, box):
    while True:
        if move in box:
            break
        else:
            print('Invalid Move!\n')
            move = input(": ")
    return move
def winner(a,sign,count):
    for i in range(3):
        if a[i][0]==a[i][1]==a[i][2]==sign:
            return sign
        elif a[0][i]==a[1][i]==a[2][i]==sign:
            return sign
        elif a[0][2]==a[1][1]==a[2][0]==sign:
            return sign
        elif a[0][0]==a[1][1]==a[2][2]==sign:
            return sign
        if count == 9:
             print('Oops --- Match Draw.\n\n---Thank You---\n')
             exit()
            

# Main
import random
import os
while True:
#  teamup Choice
    select = input('Select:\n1. You Vs Computer\n2. Player Vs Player\n:\t')
    if select == '2' or select == '1':
        while True:
#  Choice to enter names
            pnc = str(input('Continue with name as Player1 and Player2(y/n):\t'))
            # pnc ---> player name choice
            os.system('cls')
            if pnc == 'Y' or pnc == 'y':
                if select == '2':
                    player1 ='Player1'
                    player2 = 'Player2' 
                    break
                elif select == '1':
                    player1 ='Your'
                    player2 = 'Computer'
                    break
            elif pnc == 'N' or pnc == 'n':
                if select == '2':
                    player1 = input('Player1 Name:\t')
                    player2 = input('Player2 Name:\t')
                    break
                else:
                    player1= input('Your Name:\t')
                    player2=' Computer'
                    break
            else:
                print('Invalid Choice.\nTry Again.')
        break
    else:
        print('Invalid Choice.\nTry Again.')
# ------Sign Choices and Inputs------
while True:
    s = input('Choose '+player1+'s sign:\n1. X\n2. 0\n :')
    # s ---> sign
    if s == '1':
        p2sign = "X"
        p1sign = 'O'
        break
    elif s == '2':
        p1sign = 'O'
        p2sign ='X'
        break
    else:
        print('Enter a valid choice!\n')
            

# Printing Board
board(box,player1,player2,p1sign,p2sign)
count = 0
while count <= 9: 
#  Player 1 Input
    p1move = input(player1+" turn:\t")
    p1move = move_check(p1move, box2)
    box = insert(box,p1move ,p1sign)
    box2.remove(p1move)
    count = count + 1
#  Printing Board
    os.system('cls')
    board(box,player1,player2,p1sign,p2sign)
#  Winning Check
    if count >=3:
        w = winner(box,p1sign,count) 
        if w == p1sign:
            print(player1, "Win :)\n\n---Thank You for playing---")
            break
        elif w == p2sign:
            print(player2,' Wins.\n\n---Thank You for playing---')
            break
    if select == '1':
#     Computer Choices and Inputs
        p2move = random.choice(box2)
        box = insert(box,p2move,p2sign)
        os.system('cls')
        print(player2,' turn:',p2move)
    else:
#     Player 2 Move
        p2move = int(input(player2+" turn:\t"))
        p2move = move_check(p2move, box2)
    box = insert(box,p2move,p2sign)
    box2.remove(p2move)
    board(box,player1,player2,p1sign,p2sign)
    count = count + 1
#   Winning Check
    if count >=3:
        w = winner(box,p2sign,count) 
        if w == p1sign:
            print(player1, "Win :)\n\n---Thank You for playing---")
            break
        elif w == p2sign:
            print(player2,' Wins.\n\n---Thank You for playing---')
            break