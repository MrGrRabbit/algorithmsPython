
# function sum
"""
list = [2, 4, 6] 
def sum(list):
    if list == []:
        return 0
    else:
        return list[0] + sum(list[1:])
print (sum(list))
"""
# function подсчет элементов в списке
"""
list = [1, 2, 3, 4, 6]
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])
print (count(list))
"""
# Нахождение наибольшего числа в списке
"""
list = [1, 2, 5, 4]
def MAX(list):
    if(len(list) == 2):
        return list[0] if list[0] > list[1] else list[0]
    sub_max = MAX(list[1:])
    return list[0] if list[0] > sub_max else sub_max
print(MAX(list))
"""
# бинарный поиск через рекурсию
""""
list = [1, 2, 3, 4, 5]

def binSearch(list, x, start):
    if(start > len(list)):
        return -1
    mid = len(list) // 2
    if list[mid] == x:
        return mid
    elif (list[mid] > x):
        return binSearch(list[mid:], x)
    else:
        return binSearch(list[:mid], x)
print(binSearch(list, 4))
"""
# быстрая сортировка 
def quicksort(array):
    if len(array) < 2:      # base case
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i >= pivot]
        
        return quicksort(less) + [pivot] + quicksort(greater)

print (quicksort([10,5,7,11]))