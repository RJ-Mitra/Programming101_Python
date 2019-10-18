#Find Luhn's checksum special num (end digit which when added to the checksum, gives a sum which is exactly divisible by 10)

orgNum = input("Enter the original number: ")

numList = [int(x) for x in orgNum]
luhnList = []

for i in range(len(numList)):
    if i%2==1:
        temp = str(numList[i]*2)
        luhnList+=[(x) for x in temp]
    elif i%2 == 0 or i==0:
        luhnList+=(str(numList[i]))
print(luhnList)

luhnNum = 0
for i in luhnList:
    luhnNum+=int(i)

specialNum = luhnNum%10

print(specialNum)


fullNum = orgNum+str(specialNum)

print("Identification number: "+specialNum)
print("Full number: "+fullNum)

