
# lecture implementation:

def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                tmp = A[j]
                A[j] = A[j+1]
                A[j+1] = tmp


# Improved implementation:(GPT)

def bubble_sort(A):
    n = len(A)
    for i in range(n):
        swaps = False  # Flag to track if any swaps occur in the current iteration
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swaps = True

        if not swaps:
            break  # Stop the sorting process if no swaps occur in the current iteration

# Example usage:
arr = [5, 2, 9, 1, 7, 6, 3]
bubble_sort(arr)
print(arr)


"""
In this modified implementation, we introduce the swaps flag, which is initially set to False at the beginning of each 
iteration. If a swap occurs during the inner loop, the swaps flag is set to True. If, after completing an iteration, 
the swaps flag is still False, it means that no swaps were made, indicating that the sequence is already sorted. 
In such a case, we can break out of the outer loop and terminate the sorting process.

By introducing this optimization, the best-case running time complexity of the bubble sort algorithm becomes O(n), 
as the algorithm will terminate early if the input sequence is already sorted.
"""