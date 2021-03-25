
def drawfield(field):
    #savegame = open("GameProgress","a")
    for row in range(5):
        if row%2 == 0:
            actualrow = int(row/2)
            for column in range(5):
                if column%2 == 0:
                    actualcolumn = int(column/2)
                    if column == 4:
                        print(field[actualcolumn][actualrow])
                    else:
                        print(field[actualcolumn][actualrow],end ="")
                else:
                    print("|",end = "")
        else:
            for column in range(5):
               if column == 4:
                   print("-")
               else:
                    print("-",end = "")

def CheckWinner(field):
    a = False
    if field[0][0] == field[0][1] == field[0][2] and field[0][0] == field[0][1] == field[0][2] != " ":
        a = True
    elif field[1][0] == field[1][1] == field[1][2] and field[1][0] == field[1][1] == field[1][2] != " ":
         a = True
    elif field[2][0] == field[2][1] == field[2][2] and field[2][0] == field[2][1] == field[2][2] != " ": 
         a = True
    elif field[0][0] == field[1][0] == field[2][0] and field[0][0] == field[1][0] == field[2][0] != " ":
         a = True
    elif field[0][1] == field[1][1] == field[2][1] and field[0][1] == field[1][1] == field[2][1] != " ":
        a = True
    elif field[0][2] == field[1][2] == field[2][2] and field[0][2] == field[1][2] == field[2][2] != " ":
        a = True
    elif field[0][0] == field[1][1] == field[2][2] and field[0][0] == field[1][1] == field[2][2] != " ":
        a = True
    elif field[0][2] == field[1][1] == field[2][0] and field[0][2] == field[1][1] == field[2][0] != " ":
        a = True  
    return(a)


p = 1
currentfield = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
drawfield(currentfield)
while (True):
        x = int(input("player"+str(p)+" you have to enter  in which row ?\n "))
        y = int(input("player"+str(p)+" you have to enter in which column ?\n"))
        if p == 1:
           if currentfield[y][x] == " ": 
              currentfield[y][x] = "X"
              champ = p
              p = 2
           else:
                print("Invalid input. Player",str(p),"enter correct input\n")
        else:
            if currentfield[y][x] == " ":
               currentfield[y][x] = "O" 
               champ = p
               p = 1
            else:
                print("Invalid input. Player",str(p),"enter correct input\n")
        drawfield(currentfield)
        Winner = CheckWinner(currentfield)
        if Winner == True:
            print("player",str(champ)," is winner")
            break
        else:
            continue 

           




            

