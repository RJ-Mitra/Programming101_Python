#Bubble sort implementation in Python

unsortedList = []
status = True
while status:
    a = input("Enter elements to fill the unsorted array. Enter 'd' when done: ")
    if a != 'd':
        unsortedList.append(int(a))
        status = True
    else:
        status = False

print(unsortedList)

arrLen = len(unsortedList)

for i in range(arrLen):
    leastElemIndex = i
    for j in range(arrLen-i):
        if unsortedList[leastElemIndex] > unsortedList[j+i]:
                    leastElemIndex = j+i
    
    if leastElemIndex!=i:
        unsortedList[leastElemIndex], unsortedList[i] = unsortedList[i], unsortedList[leastElemIndex]
    


print(unsortedList)



#pick an elem as lowest
#compare elem to all elements in array other than itself
#if any elem<lowest, new elem becomes lowest
#At the end of loop, swap lowest with the 1st elem