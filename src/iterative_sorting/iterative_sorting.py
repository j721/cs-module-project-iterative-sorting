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

    #approach
        #starting at the beginning of the array (index = 0), 
        #compare the current element with the next element in the array
        #if current element is greater than next element
        #than swap them
            #if current element is less than the next element, move onto the next element in the list
        #repeat this loop through out the whole list once all elements have been swapped properly in order

    #created Boolean
    #want to stop passing through the list
    #as soon as we have passed the list, without swapping any elements
    is_swapped = True

    number_of_iterations = 0

    while(is_swapped):
        is_swapped = False
        #go through the list as many times as there elements and number of iterations

        #traverse through the array from starting index to n-i-1. i standing for index
        #want the last pair of elements to be (n-2, n-1). Last i elements already in place
        for i in range(len(arr)- number_of_iterations - 1):
            if arr[i] > arr[i +1]:          #swap if element found is greater than the next element in the list
                #swap
                arr[i], arr[i +1]= arr[i +1], arr[i]
                is_swapped = True       #return True once swap has ocurred
        number_of_iterations +=1        #number iterations +1, once gone through the list
        #with each consecutive iteration we can look at one less element than before
        #only need to look ath the first (n-i) + 1 elements
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

answer: time complexity is O (n+c)
space complexity is O (n +c)
'''
def counting_sort(arr, maximum=None):
    # Your code here
    #Count the number of times each value appears
    #counts[0] stores the number of 0's in the input
    #counts [4] stores the number of 4's in the input

   
    counts = [0] * (maximum +1)
    
    for i in arr:
       counts[i] +=1
    
    output =[]
    for element, count in enumerate(counts):
        if count > 0:
            for _ in range(0, count):
                output.append(element)


    return arr
