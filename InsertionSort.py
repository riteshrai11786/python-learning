# My python practice programs
# function for sorting the list of integers
def insertion_sort(L):
    # Loop over the list and sort it through insertion algo
    for index in range(1, len(L)):
        # define key, which is the current element we are using for sorting
        key = L[index]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        pivot_idx = index - 1
        # Loop over the list and compare
        while pivot_idx >= 0 and key < L[pivot_idx]:
            L[pivot_idx + 1] = L[pivot_idx]
            pivot_idx -= 1
        # assign the key to next index
        L[pivot_idx + 1] = key


# Insertion sort with recursion
def recursive_insertion_sort(L, n):
    # Base case
    if n <= 1:
        return

    # Sort n-1 elements
    recursive_insertion_sort(L, n - 1)

    '''Insert last element at its correct position 
           in sorted array.'''
    last = L[n - 1]
    j = n - 2
    # loop over the array and sort
    while j >= 0 and last < L[j]:
        L[j + 1] = L[j]
        j -= 1
    # assign the last element to original position
    L[j + 1] = last


# Driver code to test above
arr = [12, 11, 13, 5, 6]
print(arr)
insertion_sort(arr)
print("Sorted array:");
for i in range(len(arr)):
    print(arr[i], end=' ')

print()
# A utility function to print an array of size n
def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=' ')


# Driver program to test insertion sort
arr = [12, 11, 13, 5, 6]
n = len(arr)
recursive_insertion_sort(arr, n)
printArray(arr, n)
