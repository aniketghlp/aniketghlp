def checkprime(number):
    numlist = []
    output = False
    for i in range(1,10):
        #print("continuing")
        z = number%i
        if z == 0: 
           numlist.append(i)
        continue
    if len(numlist) == 2 and numlist[0] == 1 and numlist[1] == int(number):
        output = True
        print(number, "Is a prime number")
    return output 

print(checkprime(7))

