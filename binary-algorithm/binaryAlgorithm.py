# page 28
# writing a binary algorithms in python

item = int(input("Введи число для поиска: "))
def binary_search(list, item):      # The low and high variables store the boundaries of the part of the list that is search
    low = 0
    high = len(list) - 1
        
    while low <= high:              # Until this part is reduced to 1, check the middle element
        mid = (low + high)          # If the value (low + high) is odd, Python automatically
        guess = list[mid]           # turns the mid value down
        if guess == item:           # value is found
            return mid 
        if guess > item:            # many
                high = mid - 1
        else:                       # little
            low = mid + 1
            return None             # value doesn't exist

my_list = [1, 3, 5, 7, 9]  

print ("Номер числа", item ,"в массиве :", binary_search(my_list, item))

