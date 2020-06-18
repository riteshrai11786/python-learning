# Just coding practice with python
# function for sorting the list of integers
def selection_sort(L):
    # idx indicates how many items were sorted
    for idx in range(len(L)):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_idx = idx
        # We then use inner_idx to loop through the remaining elements
        for inner_idx in range(idx+1, len(L) - 1):
            # Update the min_index if the element at j is lower than it
            if L[min_idx] > L[inner_idx]:
                min_idx = inner_idx
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        L[idx], L[min_idx] = L[min_idx], L[idx]

# Test the function here
L = [3, 1, 41, 59, 26, 53, 59]
# Print the list before sorting
print(L)
# Pass the list to the sorting function
selection_sort(L)
# Let's see the list after we run the Selection Sort
print(L)

