import ctypes


class MyArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def __setitem__(self, k, value):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        self._A[k] = value
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, value):
        if not 0 <= k <= self._n:
            raise IndexError('Invalid index')
        if self._n == self._capacity:
            self._resize(2 * self._capacity)

        for i in range(self._n, k, -1):
            self._A[i] = self._A[i - 1]

        self._A[k] = value
        self._n += 1

    def remove(self, k):
        if not 0 <= k < self._n:
            raise IndexError('Invalid index')

        for i in range(k, self._n - 1):
            self._A[i] = self._A[i + 1]

        self._A[self._n - 1] = None
        self._n -= 1

        # Shrink the array if the number of elements is less than 1/4 of the capacity
        if self._n < self._capacity // 4:
            self._resize(self._capacity // 2)

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()


# Testing our code:

array = MyArray()

print(array.__len__())
array.append(10)
array.append(20)
array.append(30)
array.append(40)
print(array.__len__())
# Print the updated array
print("Array length:", len(array))
for i in range(len(array)):
    print("Element at index", i, ":", array[i])

array.remove(2)
print(array.__len__())
# Print the updated array
print("Array length:", len(array))
for i in range(len(array)):
    print("Element at index", i, ":", array[i])


array.insert(1, 55)
print(array.__len__())
# Print the updated array
print("Array length:", len(array))
for i in range(len(array)):
    print("Element at index", i, ":", array[i])

array.__setitem__(3, 99)
# Print the updated array
print("Array length:", len(array))
for i in range(len(array)):
    print("Element at index", i, ":", array[i])


"""""""""
The extended implementation adds the following methods:

__setitem__(self, k, value): This method overwrites the contents of index k with the given value.
insert(self, k, value): This method inserts the value at index k by shifting the existing elements to make room for the new element.
remove(self, k): This method removes the element at index k by shifting the elements after it to fill the gap.
The insert and remove methods also handle the resizing of the underlying array when necessary to optimize the memory usage.

Please note that the implementation assumes a zero-based index for the list elements.
"""


