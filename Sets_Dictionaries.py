

CountryList = []
for i in range(5):
    Country = input("Enter last 5 countries you visited:-")
    CountryList.append(Country)

print(CountryList)

CountrySet = set(CountryList)

print(CountrySet)

CountryDict = {}

for Country in CountryList:
    if Country not in CountryDict:
        CountryDict[Country] = 1
    else:
        CountryDict[Country] += 1


print(CountryDict)
print(CountryList[2])




