# program for comapring two equal numbers out of three
x = 1
y = 2
z = 3

#creating function so that it can accept numbers in string as well and convert them to integers and compare.
def TwoofThreeEq (x,y,z):
    x, y, z = int(x), int(y), int(z) 
    if x == y or y == z or z == x:
     output = True
    else:
        output = False
    return output

Compare1 = TwoofThreeEq(x,y,z)
Compare2 = TwoofThreeEq(1,1,1)
Compare3 = TwoofThreeEq(1,1,5)
Compare4 = TwoofThreeEq(10,'10 ',5)

print ("Compare1:-", Compare1)
print ("Compare2:-", Compare2)
print ("Compare3:-", Compare3)
print ("Compare4:-", Compare4)

# name = "5"
# countname = int(name) + 1
# print ("CN=", countname)





