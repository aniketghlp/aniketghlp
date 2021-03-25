# participantdata = []
# totalparticipant = 2
# registeredparticipant = 0
# participantfile = open("FILE.txt","w")
# #participantfile = open("FILE","a")
# while(registeredparticipant < totalparticipant):
#     tempparticipant = []
#     name = input ("Please enter your name:- ")
#     tempparticipant.append(name)
#     country = input ("Please enter country:- ")
#     tempparticipant.append(country)
#     age = input("Please enter your age:- ")
#     tempparticipant.append(int(age))
#     print (tempparticipant)
#     # add temp to part
#     participantdata.append(tempparticipant)
#     registeredparticipant   += 1
#     print(participantdata)
    
# for participant in participantdata:
#     for data in participant:
#         participantfile.write(str(data))
#         participantfile.write(" ")
#     participantfile.write("\n")

# participantfile.close()

inputfile = open("FILE.txt","r")

inputList = []
for line in inputfile:
    temppart = line.strip("\n").split()
    inputList.append(temppart)

print(inputList)

Country = {}
CountryList = []

for part in inputList:
    tempnation = part[1]
    if tempnation in Country:
        Country[tempnation] += 1
        CountryList.append(tempnation)
    else:
        Country[tempnation] = 1
        CountryList.append(tempnation)

print(Country)
GETSET = set(CountryList)
#print(CountryList)
print(GETSET)

Age = {}
for part in inputList:
    tempage = part[-1]
    if tempage in Age:
        Age[tempage] += 1
    else:
        Age[tempage] = 1

oldest = 0
youngest = 100
mostoccuringage = []
counterage = 0

for tempage in Age:
    print(tempage)
    if int(tempage) > oldest:
        oldest = int(tempage)
    if int(tempage) < youngest:
        youngest = int(tempage)
    if Age[tempage] >= counterage:
        counterage = Age[tempage]
        mostoccuringage.append(tempage)

print("Most occuring age ",mostoccuringage," with", counterage,"participants")

Line = inputfile.readline()
Line = inputfile.readline()
Line = inputfile.readline()
print(Line)


print(oldest,"  ",youngest)
        

print(Age)
inputfile.close()









