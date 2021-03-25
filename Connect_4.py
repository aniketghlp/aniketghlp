import sys
import termcolor
import colorama
from termcolor import colored, cprint
from colorama import init
init() 
###BELOW ARE FEW PRINT STATEMENTS
print(colored("""________________THIS IS A 5 * 4 CONNECT4 BOARD GAME.______________________________""",'red',attrs=['bold']))
print(colored("How to play?",'green',attrs=["underline"]))
print(colored('Please select column number 0, 1, 2, OR 3 with column 0 starting from left','yellow',attrs=['bold','dark','concealed']))
#PRINT STATEMENTS END
# Using below blank list for intitial blank board display
CD = [[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "]]  
# Below is the function to check winner of the game
def checkwinner(board):
    a = False
    if board[0][4] == board[0][3] == board[0][2] == board[0][1] and board[0][4] == board[0][3] == board[0][2] == board[0][1] != " ":
        a = True
    elif board[0][4] == board[1][4] == board[2][4] == board[3][4] and board[0][4] == board[1][4] == board[2][4] == board[3][4] != " ":
        a = True
    elif board[0][4] == board[1][3] == board[2][2] == board[3][1] and board[0][4] == board[1][3] == board[2][2] == board[3][1] != " ":
        a = True
    elif board[0][3] == board[0][2] == board[0][1] == board[0][0] and board[0][3] == board[0][2] == board[0][1] == board[0][0] != " ":
        a = True
    elif board[0][3] == board[1][3] == board[2][3] == board[3][3] and board[0][3] == board[1][3] == board[2][3] == board[3][3] != " ":
        a = True
    elif board[0][3] == board[1][2] == board[2][1] == board[3][0] and board[0][3] == board[1][2] == board[2][1] == board[3][0] != " ":
        a = True
    elif board[0][2] == board[1][2] == board[2][2] == board[3][2] and board[0][2] == board[1][2] == board[2][2] == board[3][2] != " ":
        a = True
    elif board[0][1] == board[1][1] == board[2][1] == board[3][1] and board[0][1] == board[1][1] == board[2][1] == board[3][1] != " ":
        a = True
    elif board[0][1] == board[1][2] == board[2][3] == board[3][4] and board[0][1] == board[1][2] == board[2][3] == board[3][4] != " ":
        a = True
    elif board[0][0] == board[1][0] == board[2][0] == board[3][0] and board[0][0] == board[1][0] == board[2][0] == board[3][0] != " ":
        a = True
    elif board[0][0] == board[1][1] == board[2][2] == board[3][3] and board[0][0] == board[1][1] == board[2][2] == board[3][3] != " ":
        a = True
    elif board[1][4] == board[1][3] == board[1][2] == board[1][1] and board[1][4] == board[1][3] == board[1][2] == board[1][1] != " ":
        a = True
    elif board[1][3] == board[1][2] == board[1][1] == board[1][0] and board[1][3] == board[1][2] == board[1][1] == board[1][0] != " ":
        a = True
    elif board[2][4] == board[2][3] == board[2][2] == board[2][1] and board[2][4] == board[2][3] == board[2][2] == board[2][1] != " ":
        a = True
    elif board[2][3] == board[2][2] == board[2][1] == board[2][0] and board[2][3] == board[2][2] == board[2][1] == board[2][0] != " ":
        a = True
    elif board[3][4] == board[3][3] == board[3][2] == board[3][1] and board[3][4] == board[3][3] == board[3][2] == board[3][1] != " ":
        a = True
    elif board[3][3] == board[3][2] == board[3][1] == board[3][0] and board[3][3] == board[3][2] == board[3][1] == board[3][0] != " ":
        a = True
    else:
        a = False
    return(a)
# below is the functions that draws/displays the board
def board5x4(field):
    for r in range(9):
        if r%2 == 0:
            row = int(r/2)            
            for c in range(0,7):
                col = int(c/2)
                if c%2 == 0 and c == 6:
                    print(field[3][row])
                elif c%2 != 0:
                    print("|",end="")
                else:
                    print(field[col][row],end="")
        else:
            for c in range(0,7):
                if c == 6:
                    print("-")
                else:
                    print("-",end="")
board5x4(CD)  
# Below is the main program to get input from the players and checks the winner
#C1 = C2 = C3 = C4 = 5
P = 1#Player 1 initiated
R1 = R2 = R3 = R4  = 4
while True:
    if (P == 1):
        I = int(input("Player "+str(P)+" enter the column(0,1,2,3)in which you want to put yellow ◍ :- "))
        if I == 0 and R1 >= 0:
            #R = 4
            #if CD[I][R1] == " ":
            CD[I][R1] = colored(u'\u25CD','yellow')
            R1 -= 1 
            champ = P
            P = 2
            #R -= 1
        elif I == 1 and R2 >= 0:
            CD[I][R2] = colored(u'\u25CD','yellow')
            R2 -= 1 
            champ = P
            P = 2
        elif I == 2 and  R3 >= 0:
            CD[I][R3] = colored(u'\u25CD','yellow')
            R3 -= 1 
            champ = P
            P = 2  
        elif I == 3 and R4 >= 0:
            CD[I][R4] = colored(u'\u25CD','yellow')
            R4 -= 1 
            champ = P
            P = 2  
        else:
            print(colored("ERROR : the column number is invalid or the column is full, please select another",'yellow','on_red'))
            P = 1
    else:
        I = int(input("Player "+str(P)+" enter the column(0,1,2,3)in which you want to put green ◍ :- "))
        if I == 0 and R1 >= 0:
            #R = 4
            #if CD[I][R1] == " ":
            CD[I][R1] = colored(u'\u25CD','green')
            R1 -= 1 
            champ = P
            P = 1
            #R -= 1
        elif I == 1 and R2 >= 0:
            CD[I][R2] = colored(u'\u25CD','green')
            R2 -= 1 
            champ = P
            P = 1
        elif I == 2 and R3 >= 0:
            CD[I][R3] = colored(u'\u25CD','green')
            R3 -= 1 
            champ = P
            P = 1  
        elif I == 3 and R4 >= 0:
            CD[I][R4] = colored(u'\u25CD','green')
            R4 -= 1 
            champ = P
            P = 1  
        else:
            print(colored("ERROR : the column number is invalid or the column is full, please select another",'yellow','on_red'))
            P = 2
    board5x4(CD)
    winner = checkwinner(CD)
    if winner == True:
        if champ == 1:
            print(colored("Player ",'yellow',attrs=['bold','dark'])+colored(champ,'yellow',attrs=['dark','bold'])+colored(" Is the winner of this game",'yellow',attrs=['bold','dark']))
            break
        else:
            print(colored("Player ",'green',attrs=['bold','dark'])+colored(champ,'green',attrs=['dark','bold'])+colored(" Is the winner of this game",'green',attrs=['bold','dark']))
            break
    elif R1 == R2 == R3 == R4 == -1:
        print(colored("Board is full, NO WINNER, start new game",'cyan',attrs=['bold','dark']))
        break
    else:
        continue







