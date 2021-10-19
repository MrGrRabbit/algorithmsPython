# Sorting by selection on python
#
#                                        page 58 chapter 2
#---------------------------------------------------------


def find_smallest(arr):
    smallest = arr[0]       # to store the lowest value
    smallest_index = 0      # to store the lowest value index
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):     # function for array sorting
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)   # finds the smallest element in the array and adds it to the new array
        newArr.append(arr.pop(smallest))
    return newArr

print (selectionSort([5, 3, 2, 9, 10]))

