"""
To implement a pop method for the DynamicArray class that removes the last element and shrinks the capacity of the array
 by half whenever the number of elements goes below N/4, you can add the following method to the class:
"""
from DynamicArrayImplementation import MyArray


def pop(self):
    if self._n == 0:
        raise IndexError('pop from empty array')

    element = self._A[self._n - 1]
    self._A[self._n - 1] = None
    self._n -= 1

    # Shrink the array if the number of elements is less than 1/4 of the capacity
    if self._n < self._capacity // 4:
        self._resize(self._capacity // 2)

    return element


"""
In this implementation, the pop method first checks if the array is empty (self._n == 0). If it is empty, an IndexError 
is raised to indicate that there are no elements to remove.

If the array is not empty, the last element (self._A[self._n - 1]) is retrieved and stored in the element variable. 
The last position in the array is then set to None, and the size _n is decremented.

After removing the element, the method checks if the number of elements is less than 1/4 of the capacity 
(self._n < self._capacity // 4). If this condition is met, the _resize method is called to shrink the capacity of the 
array by half.

Finally, the element is returned, representing the removed element from the array.

Now you can use the pop method to remove the last element from the array and automatically resize the array when necessary.

Example usage:
"""

# use the implementation in file 9.2 to run the tests successfully
dynamic_array = MyArray()
dynamic_array.append(10)
dynamic_array.append(20)
dynamic_array.append(30)

print(dynamic_array.pop())  # Output: 30

print(len(dynamic_array))  # Output: 2


# ---------------------------------------------------------------------------------
# C-5.25

"""
you can implement the removal of all occurrences of a specific value from a list using a different approach by 
creating a new list that only includes the elements that are not equal to the value you want to remove. 
Here's an alternative implementation:
"""

def remove_all(data, value):
    data[:] = [x for x in data if x != value]

"""
In this implementation, we use a list comprehension to create a new list that only includes the elements from data that
are not equal to the specified value. By assigning this new list back to data[:], we effectively replace the contents 
of the original list with the updated list.

This approach also has a worst-case running time of O(n), as it needs to iterate through each element in the original 
list once to create the new list. However, it may require additional memory to store the new list temporarily.

Here's an example usage of this alternative implementation:
"""

data = [1, 2, 3, 2, 4, 2, 5]
remove_all(data, 2)
print(data)  # Output: [1, 3, 4, 5]
