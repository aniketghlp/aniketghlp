SongDict = {}

SongDict["Song"] = "That's my name"
SongDict["Artist"] = "Akcent"
SongDict["Album"] = SongDict["Song"]
SongDict["MusicCompany"] = "Ultra Records"
SongDict["Released"] = "2009"
SongDict["Minutes"] = "4"
SongDict["Seconds"] = "6"
SongDict["ProducedBy"] = "Edward Maya"
SongDict["Genres"] = "Dance Pop "


#print(SongDict)

for key in SongDict:
        print(key,":- ", SongDict[key])

print("*********************************Below output is for guess function***************************** ")

def guess(key,value):
    if key in SongDict and value == SongDict[key]:
        #print(key)
        output = True
    else:
        output = False
    return output

print("try guessing about my favourite song")
for key in SongDict:
    print(" Guess ",key,"?")
    a = guess(key,input())
    if a == True:
      print("Correct answer")
    else:
        print("Wrong answer")
        print("Correct answer is :-", SongDict[key] )
        


      





