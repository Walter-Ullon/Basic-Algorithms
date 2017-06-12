def find_smallest(myList):
    smallest = myList[0]
    smallestIndex = 0

    for i in range(1, len(myList)):
        if myList[i] < smallest:
            smallest = myList[i]
            smallestIndex = i
    return smallestIndex


def selection_sort(myList):
    newList = []
    for i in range(len(myList)):
        smallest = find_smallest(myList)
        newList.append(myList.pop(smallest))
    return newList



alist = [3, 2, 5, 1, 4, 11, 9]

print selection_sort(alist)