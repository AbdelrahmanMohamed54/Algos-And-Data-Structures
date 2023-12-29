# Implement a randomized quicksort, which randomly picks the pivot element. This algorithm has a
# worst-case expected running time complexity of O(n log n).

import random

def randomized_quick_sort(S):
    if len(S) <= 1:
        return S

    left = []
    right = []
    pivot_index = random.randint(0, len(S) - 1)
    pivot = S[pivot_index]

    for i, element in enumerate(S):
        if i == pivot_index:
            continue
        if element >= pivot:
            right.append(element)
        else:
            left.append(element)

    left = randomized_quick_sort(left)
    right = randomized_quick_sort(right)

    return left + [pivot] + right

# Example usage:
arr = [5, 2, 9, 1, 7, 6, 3]
sorted_arr = randomized_quick_sort(arr)
print(sorted_arr)


"""
In this modified implementation, the random.randint() function is used to generate a random index within the range of 
the input sequence. The element at the randomly chosen index is selected as the pivot. The remaining code follows the 
same logic as the given quicksort implementation.

By randomly selecting the pivot element, we achieve the expected running time complexity of O(n log n) in the worst 
case, as stated in the requirement.
"""