# In the exam you will need to calculate the time complexity using Recurrence relations or using master theorem

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


"""
The running time complexity of this implementation is O(n), where n is the exponent. This is because for each recursive 
call, the function reduces the exponent by 1 until it reaches the base case (n = 0), resulting in a total of n recursive 
calls. Therefore, the time complexity grows linearly with the exponent.

It's worth noting that this implementation is not efficient for large exponents since it performs repetitive computation 
Using more efficient algorithms like the exponentiation by squaring method can significantly reduce the running time 
complexity for calculating large powers.
"""