# program for FizzBuzz and prime number between 1 to 100
# intialising variable number to 1
number = 1

prime = [] # defining empty list for prime numbers
Fizz = []
Buzz = []

# defining function to check if a number is prime or not, if yes it returns a value TRUE else FALSE
def checkprime(number):
    numlist = []
    output = False
    for i in range(1,101):
        #print("continuing")
        z = number%i        # modulo of number 
        if z == 0: 
           numlist.append(i)
        continue
    if len(numlist) == 2 and numlist[0] == 1 and numlist[1] == int(number):# If statment to check prime number
        output = True
        #print(number, "Is a prime number")
    return output

while number <= 100:
    x = number%3 # checking if number divisible by 3
    y = number%5 # checking if number divisible by 5
     
    if x == 0 and y == 0: # checking if number divisible by 3 and 5
      print ("FizzBuzz")
      Fizz.append(number)
      Buzz.append(number)
    elif x == 0:          # checking if number divisible by 3
      print ("Fizz") 
      Fizz.append(number)
    elif y == 0:          # checking if number divisible by 5
      print ("Buzz")
      Buzz.append(number)
    else: 
      print (number)
    z = checkprime(number)
    if z == True:         # If number is prime adding to the prime list  
          prime.append(number)
    number += 1

print("prime numbers", prime)
#print("number divisible by 3", Fizz)
#print("number divisible by 5", Buzz)





         