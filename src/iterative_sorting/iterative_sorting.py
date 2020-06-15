# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    #i variable indicates how many items were sorted
    for i in range(0, len(arr) - 1):
        #to find the minimum value of the unsorted array
        #assume that the first element is the lowest
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        #nested for loop with x to traverse through the remaining elements
        for x in range( i+1, len(arr)):         #range (increments value of i variable, to length of array)
            if arr [smallest_index] > arr[x]:   # update the smallest_index if the element at x in unsorted array is lower than it
                smallest_index = x               #smallest_index now becomes x element, since it's value was smaller than it   

        # TO-DO: swap
        # Your code here

        #after finding lowest item in the unsorted array, swap with the first unsorted item 
        #order has been swapped 
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swapped = True

    while(swapped):
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i +1]:
                #swap
                arr[i], arr[i +1]= arr[i +1], arr[i]
                swapped = True
    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
