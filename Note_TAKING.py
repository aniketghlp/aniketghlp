### this program doesnot checks actually directory, instead when it runs  it creates the first file name, when the same filename is 
## it is recalled or retyped by the user it asks for other options
checkname = []
def checkfileexistance(filename):#Function to check filename already exist or not
    output = False
    for name in checkname:
        if name == NewFileName:
            print("file exist")
            output = True
            break
    return(output)

def CallOpt4(lineno,NewText):#Function for option 4 to select a line and replace it with new text
    NewFile = open(NewFileName,"r+")
    a = []
    #print(a)
    for line in NewFile:
        #print(line)
        a.append(line)
    #print(a)
    b = a[lineno-1]
    a[lineno-1] = b.replace(b,NewText+"\n")
    #print(a)
    NewFile.close()
    NewFile = open(NewFileName,"w")
    for element in a:
        NewFile.writelines(element)
    NewFile.close()
    NewFile = open(NewFileName,"r")
    show = NewFile.read()
    print(show)
    NewFile.close()
    #return (NewFile)
    
def NextTodo(a):#function runs when filename already exists it displays the options and act according to the section
    if a == True:
        print("File name already exist")
        print("Please choose below options ")
        option = input("1.Read the file\n 2.Delete the file and startover.\n 3.Append the file.\n 4.Replace a line Please select option 1,2,3 or 4:-")
        print(option)
        if option == "1":
            NewFile = open(NewFileName,"r")
            read = NewFile.read()
            print(read)
            NewFile.close()
        elif option == "2":
            NewFile = open(NewFileName,"w")
            EnterText = input("Please enter text here")
            NewFile.write(EnterText+"\n")
            NewFile.close()
        elif option == "3":
            NewFile = open(NewFileName,"a")
            EnterText = input("Please enter text here\n")
            NewFile.write(EnterText+"\n")
            NewFile.close()
        else:
            lineno = int(input("Please enter the line no to be replaced"))
            NewText = input("Please input new text")
            CallOpt4(lineno,NewText)        
    else:
        checkname.append(NewFileName)
        NewFile = open(NewFileName,"w")
        EnterText = input("Please enter text here\n")
        NewFile.write(EnterText+"\n")
        NewFile.close()

#below is the main program that starts with the new file if user enter Y, then again asks for new File if same 
#filename is enterd options are displayed
# NOTE:- After entering text and pressing enter it is considerd as new line.
while True:
    Choice = input("Do you want to create a file (Y/N)?")
    if Choice == "Y":
        NewFileName = input("Please enter new file name?")
        a = checkfileexistance(NewFileName)
        NextTodo(a)
    else:
        break







 





