# Python program for merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2 # finding a middle element from an array
        L = arr[:mid] # dividing an array for left
        R = arr[mid:] # and right parts
        # apply merge sort into divded arrays
        merge_sort(L)
        merge_sort(R)
        # initialize 3 variables to deal with divided arrays
        i = j = k = 0
        # Copy data from L and R arrays to the temp array
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        # Checking if any elements was left
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1


# Code to print the list
def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    print_list(arr)
    merge_sort(arr)
    print("Sorted array is: ", end="\n")
    print_list(arr)


