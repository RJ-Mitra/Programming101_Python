#insertion sort

#picks an element
#compares it to left elem
#if it is lesser, compares to left of left elem and so on
#inserts if left elem is lesser than it

#[23,1,34,2,67,3,99]
def insertionSort(unsortedArray):
    for i in range(1,len(unsortedArray)):
        tempVal = unsortedArray[i]
        index = i
        while index > 0 and tempVal<unsortedArray[index-1]:
            unsortedArray[index] = unsortedArray[index-1]
            index = index - 1
            unsortedArray[index] = tempVal
    return unsortedArray


print(insertionSort([23,1,34,2,67,3,99]))