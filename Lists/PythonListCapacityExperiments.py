"""
R-5.1 Execute the experiment from Code Fragment 5.1 and compare the results
on your system to those we report in Code Fragment 5.2.

R-5.2 In Code Fragment 5.1, we perform an experiment to compare the length of
a Python list to its underlying memory usage. Determining the sequence
of array sizes requires a manual inspection of the output of that program.
Redesign the experiment so that the program outputs only those values of
k at which the existing capacity is exhausted. For example, on a system
consistent with the results of Code Fragment 5.2, your program should
output that the sequence of array capacities are 0, 4, 8, 16, 25, . . . .

R-5.3 Modify the experiment from Code Fragment 5.1 in order to demonstrate
that Python’s list class occasionally shrinks the size of its underlying array
when elements are popped from a list.
"""


# R-5.1

import sys  # provides getsizeof function

data = []
for k in range(26):  # NOTE: must fix choice of n
    a = len(data)  # number of elements
    b = sys.getsizeof(data)  # actual size in bytes
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)

# R-5.2

data = []
capacity = 0
for k in range(26):
    if len(data) == capacity:
        print("Capacity exhausted at k =", k)
        capacity = (capacity + 1) * 2  # Double the capacity
    data.append(None)

# R-5.3

import sys

data = []
for k in range(26):
    a = len(data)  # number of elements
    b = sys.getsizeof(data)  # actual size in bytes
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)

    if k % 4 == 0 and k > 0:
        data.pop()  # Remove the last element every 4 iterations
