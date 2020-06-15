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
    high = len(arr) -1

    while low <= high:
        middle = (low+ high)//2
        guess = arr[middle]     
        if guess == target:
            return middle
        if guess > target:
            high = middle -1
        else:
            low = middle +  1
    return -1  # not found
