# Implements basic "Binary Search" Algorithm


def binary_search(myList, item):
    index = len(myList)
    minim = 0
    maxim = index - 1

    while minim <= maxim:
        mid = (minim + maxim) / 2
        guess = myList[mid]         # if not integer, python rounds down

        if guess == item:
            return mid
        if guess > item:
            maxim = mid - 1
        if guess < item:
            minim = mid + 1

    return None


# TEST -------------------
myList1 = [3, 5, 7, 9, 11, 13]
print 'The item you\'re looking for is at index ' + str(binary_search(myList1, 11))

