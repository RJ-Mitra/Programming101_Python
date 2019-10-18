#Special number check

orgNum = input("Enter the original number: ")

numList = [int(x) for x in orgNum]
specialNum = orgNum[len(orgNum)-1]

luhnList = []

for i in range(len(numList)-1):
    if i%2==1:
        temp = str(numList[i]*2)
        luhnList+=[(x) for x in temp]
    elif i%2 == 0 or i==0:
        luhnList+=(str(numList[i]))

print(luhnList)

luhnNum = 0
for i in luhnList:
    luhnNum+=int(i)

if luhnNum%10 == 0:
    calcSpecialNum = (luhnNum%10)
else:
    calcSpecialNum = 10-(luhnNum%10)

if int(calcSpecialNum) != int(specialNum):
    print("Invalid Number")
else:
    print("Valid number")
