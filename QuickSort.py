def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


# Test ------------------------------
myArr = [5, 3, 3, 1, 11, 15, 3, 2, 4]
print quick_sort(myArr)