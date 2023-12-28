# use the implementation in file DynamicArrayImplementation.py to run the tests successfully
from DynamicArrayImplementation import MyArray


def __getitem__(self, k):
    if isinstance(k, int):
        if k < 0:
            k += self._n
        if not 0 <= k < self._n:
            raise IndexError('Invalid index')
        return self._A[k]
    else:
        raise TypeError('Invalid index type')


"""
In the modified code, we first check if k is an integer using the isinstance() function. 
If it is an integer, we proceed to handle the negative index case.

If k is negative, we add self._n to it to convert it into a positive index. This allows us to access elements relative 
to the end of the array. For example, -1 refers to the last element, -2 refers to the second-to-last element, and so on.

After converting the negative index to a positive index, we perform the range check to ensure it is a valid index within 
the bounds of the array.

If k is not an integer or if it is still outside the valid index range after converting a negative index, we raise an 
IndexError with an appropriate error message.

Now you can use both positive and negative indices when accessing elements of the array. For example:
"""


my_array = MyArray()
my_array.append(10)
my_array.append(20)
my_array.append(30)
my_array.append(40)

print(my_array[0])    # Output: 10
print(my_array[-1])   # Output: 40
print(my_array[-2])   # Output: 30


"""
In this example, my_array[0] returns the first element (10), my_array[-1] returns the last element (40), and 
my_array[-2] returns the second-to-last element (30).
"""
