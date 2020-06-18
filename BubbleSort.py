# Just coding practice with python
# function for sorting the list of integers
def bubble_sort(L):
    # idx indicates how many items were sorted
    for idx in range(len(L)):
        # We then use inner_idx to loop through the remaining elements
        for inner_idx in range(idx + 1, len(L) - 1):
            if L[idx] > L[inner_idx]:
                # After finding the lowest item of the adjusnt element, swap with the first unsorted item
                L[idx], L[inner_idx] = L[inner_idx], L[idx]


# Python Program for implementation of
# Recursive Bubble sort
def recursive_bubble_sort(L):
    for indx, num in enumerate(L):
        try:
            if L[indx + 1] < num:
                L[indx] = L[indx + 1]
                L[indx + 1] = num
                recursive_bubble_sort(L)
        except IndexError:
            pass
    return L

# Test the function here
L = [3, 1, 41, 59, 26, 53, 59]
# Print the list before sorting
print(L)
# Pass the list to the sorting function
bubble_sort(L)
# Let's see the list after we run the Selection Sort
print(L)

print("************************************************")
print(" Test Recursive Bubble sort")
print("************************************************")

L = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(L)

print("Sorted array:");
for i in range(0, len(L)):
    print(L[i], end=' ')
