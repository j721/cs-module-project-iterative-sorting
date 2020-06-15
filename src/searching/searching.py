def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        #if array i value matches with the target value. then return the element i.
        if arr[i] == target:      
            return i    

    return -1   # Else not found. Similar to return None


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) -1          #length of array all the way to last element in index

    while low <= high:              #low less than or equal to high(i.e. length of the array)
        middle = (low+ high)//2
        guess = arr[middle]     #guess starts with search in the middle index
        if guess == target:     #if target is actually the middle index then just return it
            return middle       
        if guess > target:      #if guess is larger than the target, then decrease guess by -1
            high = middle -1
        else:
            low = middle +  1   # if guess is smaller than target, then increase by + 1
    return -1  # not found     
