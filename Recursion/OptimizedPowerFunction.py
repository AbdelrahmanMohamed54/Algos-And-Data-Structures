# Solution on page 172 - 173 in the goodrich book

def power(x, n):
    """Compute the value x n for integer n."""
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)      # rely on truncated division
        result = partial*partial
    if n % 2 == 1:                      # if n odd, include extra factor of x
        result *= x
    return result


# In the exam you will need to calculate the time complexity using Recurrence relations or using master theorem

"""
To analyze the running time of the revised algorithm, we observe that the exponent
in each recursive call of function power(x,n) is at most half of the preceding
exponent. As we saw with the analysis of binary search, the number of times that
we can divide n in half before getting to one or less is O(logn). Therefore, our new
formulation of the power function results in O(logn) recursive calls. Each individual
activation of the function uses O(1) operations (excluding the recursive calls),
and so the total number of operations for computing power(x,n) is O(logn). This
is a significant improvement over the original O(n)-time algorithm.

The improved version also provides significant saving in reducing the memory
usage. The first version has a recursive depth of O(n), and therefore O(n) activation
records are simultaneous stored in memory. Because the recursive depth of the
improved version is O(logn), its memory usages is O(logn) as well.
"""